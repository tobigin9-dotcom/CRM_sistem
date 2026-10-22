from django import forms
from django.db.models import Q

from contracts.models import Contract
from leads.models import Lead
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["lead", "contract"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        available_leads = Lead.objects.filter(customer__isnull=True)
        available_contracts = Contract.objects.filter(customer__isnull=True)
        if self.instance.pk:
            available_leads = Lead.objects.filter(
                Q(customer__isnull=True) | Q(customer=self.instance)
            )
            available_contracts = Contract.objects.filter(
                Q(customer__isnull=True) | Q(customer=self.instance)
            )
        self.fields["lead"].queryset = available_leads
        self.fields["contract"].queryset = available_contracts

    def clean(self):
        cleaned = super().clean()
        lead = cleaned.get("lead")
        contract = cleaned.get("contract")
        if lead:
            lead_matches = Customer.objects.filter(lead=lead)
            if self.instance.pk:
                lead_matches = lead_matches.exclude(pk=self.instance.pk)
            if lead_matches.exists():
                self.add_error("lead", "Этот потенциальный клиент уже активирован.")
        if contract:
            contract_matches = Customer.objects.filter(contract=contract)
            if self.instance.pk:
                contract_matches = contract_matches.exclude(pk=self.instance.pk)
            if contract_matches.exists():
                self.add_error("contract", "Этот контракт уже привязан к клиенту.")
        return cleaned

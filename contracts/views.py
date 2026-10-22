from core.views import BaseCreateView, BaseDeleteView, BaseDetailView, BaseListView, BaseUpdateView
from .forms import ContractForm
from .models import Contract


class ContractListView(BaseListView):
    model = Contract
    context_object_name = "contracts"
    template_name = "contracts/contracts-list.html"
    permission_required = "contracts.view_contract"


class ContractDetailView(BaseDetailView):
    model = Contract
    template_name = "contracts/contracts-detail.html"
    permission_required = "contracts.view_contract"


class ContractCreateView(BaseCreateView):
    model = Contract
    form_class = ContractForm
    template_name = "contracts/contracts-create.html"
    permission_required = "contracts.add_contract"
    success_url = "/contracts/"


class ContractUpdateView(BaseUpdateView):
    model = Contract
    form_class = ContractForm
    template_name = "contracts/contracts-edit.html"
    permission_required = "contracts.change_contract"
    success_url = "/contracts/"


class ContractDeleteView(BaseDeleteView):
    model = Contract
    template_name = "contracts/contracts-delete.html"
    permission_required = "contracts.delete_contract"
    success_url = "/contracts/"

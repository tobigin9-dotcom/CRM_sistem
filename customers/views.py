from core.views import BaseCreateView, BaseDeleteView, BaseDetailView, BaseListView, BaseUpdateView
from .forms import CustomerForm
from .models import Customer


class CustomerListView(BaseListView):
    model = Customer
    context_object_name = "customers"
    template_name = "customers/customers-list.html"
    permission_required = "customers.view_customer"

    def get_queryset(self):
        return super().get_queryset().select_related("lead", "contract")


class CustomerDetailView(BaseDetailView):
    model = Customer
    template_name = "customers/customers-detail.html"
    permission_required = "customers.view_customer"


class CustomerCreateView(BaseCreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customers-create.html"
    permission_required = "customers.add_customer"
    success_url = "/customers/"


class CustomerUpdateView(BaseUpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customers-edit.html"
    permission_required = "customers.change_customer"
    success_url = "/customers/"


class CustomerDeleteView(BaseDeleteView):
    model = Customer
    template_name = "customers/customers-delete.html"
    permission_required = "customers.delete_customer"
    success_url = "/customers/"

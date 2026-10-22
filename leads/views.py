from core.views import BaseCreateView, BaseDeleteView, BaseDetailView, BaseListView, BaseUpdateView
from .forms import LeadForm
from .models import Lead


class LeadListView(BaseListView):
    model = Lead
    context_object_name = "leads"
    template_name = "leads/leads-list.html"
    permission_required = "leads.view_lead"

    def get_queryset(self):
        return super().get_queryset().select_related("advertisement").prefetch_related("customer")


class LeadDetailView(BaseDetailView):
    model = Lead
    template_name = "leads/leads-detail.html"
    permission_required = "leads.view_lead"


class LeadCreateView(BaseCreateView):
    model = Lead
    form_class = LeadForm
    template_name = "leads/leads-create.html"
    permission_required = "leads.add_lead"
    success_url = "/leads/"


class LeadUpdateView(BaseUpdateView):
    model = Lead
    form_class = LeadForm
    template_name = "leads/leads-edit.html"
    permission_required = "leads.change_lead"
    success_url = "/leads/"


class LeadDeleteView(BaseDeleteView):
    model = Lead
    template_name = "leads/leads-delete.html"
    permission_required = "leads.delete_lead"
    success_url = "/leads/"

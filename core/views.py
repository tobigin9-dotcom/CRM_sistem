from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Count, ProtectedError, Sum
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from advertisements.models import Advertisement
from contracts.models import Contract
from customers.models import Customer
from leads.models import Lead
from products.models import Product


def logout_view(request):
    """Logout endpoint compatible with the existing navigation template."""
    logout(request)
    return redirect("login")


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "users/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            products_count=Product.objects.count(),
            advertisements_count=Advertisement.objects.count(),
            leads_count=Lead.objects.count(),
            customers_count=Customer.objects.count(),
        )
        return context


class BaseListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    context_object_name = None
    template_name = ""
    permission_required = ""


class BaseDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = ""
    permission_required = ""


class BaseCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = ""
    permission_required = ""


class BaseUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = ""
    permission_required = ""


class BaseDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = ""
    permission_required = ""

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            messages.error(self.request, "Нельзя удалить запись: с ней связаны другие данные.")
            return HttpResponseRedirect(self.get_success_url())


class AdvertisementStatisticsView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Advertisement
    template_name = "ads/ads-statistic.html"
    context_object_name = "ads"
    permission_required = "advertisements.view_advertisement"

    def get_queryset(self):
        return Advertisement.objects.select_related("product").annotate(
            leads_count=Count("leads", distinct=True),
            customers_count=Count("leads__customer", distinct=True),
            revenue=Sum("leads__customer__contract__cost"),
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for advertisement in context["ads"]:
            revenue = advertisement.revenue or 0
            advertisement.profit = (
                revenue / advertisement.budget if advertisement.budget else None
            )
        return context

from core.views import (
    AdvertisementStatisticsView, BaseCreateView, BaseDeleteView,
    BaseDetailView, BaseListView, BaseUpdateView,
)
from .forms import AdvertisementForm
from .models import Advertisement


class AdvertisementListView(BaseListView):
    model = Advertisement
    context_object_name = "ads"
    template_name = "ads/ads-list.html"
    permission_required = "advertisements.view_advertisement"


class AdvertisementDetailView(BaseDetailView):
    model = Advertisement
    template_name = "ads/ads-detail.html"
    permission_required = "advertisements.view_advertisement"


class AdvertisementCreateView(BaseCreateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = "ads/ads-create.html"
    permission_required = "advertisements.add_advertisement"
    success_url = "/ads/"


class AdvertisementUpdateView(BaseUpdateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = "ads/ads-edit.html"
    permission_required = "advertisements.change_advertisement"
    success_url = "/ads/"


class AdvertisementDeleteView(BaseDeleteView):
    model = Advertisement
    template_name = "ads/ads-delete.html"
    permission_required = "advertisements.delete_advertisement"
    success_url = "/ads/"

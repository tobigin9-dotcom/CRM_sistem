from django.urls import path
from . import views

urlpatterns = [
    path("", views.AdvertisementListView.as_view(), name="ad-list"),
    path("new", views.AdvertisementCreateView.as_view(), name="ad-create"),
    path("new/", views.AdvertisementCreateView.as_view()),
    path("statistic", views.AdvertisementStatisticsView.as_view(), name="ad-statistic"),
    path("statistic/", views.AdvertisementStatisticsView.as_view()),
    path("statistics/", views.AdvertisementStatisticsView.as_view(), name="stats"),
    path("<int:pk>", views.AdvertisementDetailView.as_view(), name="ad-detail"),
    path("<int:pk>/", views.AdvertisementDetailView.as_view()),
    path("<int:pk>/edit", views.AdvertisementUpdateView.as_view(), name="ad-update"),
    path("<int:pk>/edit/", views.AdvertisementUpdateView.as_view()),
    path("<int:pk>/delete", views.AdvertisementDeleteView.as_view(), name="ad-delete"),
    path("<int:pk>/delete/", views.AdvertisementDeleteView.as_view()),
]

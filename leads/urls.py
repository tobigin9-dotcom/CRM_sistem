from django.urls import path
from . import views

urlpatterns = [
    path("", views.LeadListView.as_view(), name="lead-list"),
    path("new", views.LeadCreateView.as_view(), name="lead-create"),
    path("new/", views.LeadCreateView.as_view()),
    path("<int:pk>", views.LeadDetailView.as_view(), name="lead-detail"),
    path("<int:pk>/", views.LeadDetailView.as_view()),
    path("<int:pk>/edit", views.LeadUpdateView.as_view(), name="lead-update"),
    path("<int:pk>/edit/", views.LeadUpdateView.as_view()),
    path("<int:pk>/delete", views.LeadDeleteView.as_view(), name="lead-delete"),
    path("<int:pk>/delete/", views.LeadDeleteView.as_view()),
]

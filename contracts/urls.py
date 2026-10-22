from django.urls import path
from . import views

urlpatterns = [
    path("", views.ContractListView.as_view(), name="contract-list"),
    path("new", views.ContractCreateView.as_view(), name="contract-create"),
    path("new/", views.ContractCreateView.as_view()),
    path("<int:pk>", views.ContractDetailView.as_view(), name="contract-detail"),
    path("<int:pk>/", views.ContractDetailView.as_view()),
    path("<int:pk>/edit", views.ContractUpdateView.as_view(), name="contract-update"),
    path("<int:pk>/edit/", views.ContractUpdateView.as_view()),
    path("<int:pk>/delete", views.ContractDeleteView.as_view(), name="contract-delete"),
    path("<int:pk>/delete/", views.ContractDeleteView.as_view()),
]

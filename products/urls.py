from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product-list"),
    path("new", views.ProductCreateView.as_view(), name="product-create"),
    path("new/", views.ProductCreateView.as_view()),
    path("<int:pk>", views.ProductDetailView.as_view(), name="product-detail"),
    path("<int:pk>/", views.ProductDetailView.as_view()),
    path("<int:pk>/edit", views.ProductUpdateView.as_view(), name="product-update"),
    path("<int:pk>/edit/", views.ProductUpdateView.as_view()),
    path("<int:pk>/delete", views.ProductDeleteView.as_view(), name="product-delete"),
    path("<int:pk>/delete/", views.ProductDeleteView.as_view()),
]

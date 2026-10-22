from core.views import BaseCreateView, BaseDeleteView, BaseDetailView, BaseListView, BaseUpdateView
from .forms import ProductForm
from .models import Product


class ProductListView(BaseListView):
    model = Product
    context_object_name = "products"
    template_name = "products/products-list.html"
    permission_required = "products.view_product"


class ProductDetailView(BaseDetailView):
    model = Product
    template_name = "products/products-detail.html"
    permission_required = "products.view_product"


class ProductCreateView(BaseCreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/products-create.html"
    permission_required = "products.add_product"
    success_url = "/products/"


class ProductUpdateView(BaseUpdateView):
    model = Product
    form_class = ProductForm
    template_name = "products/products-edit.html"
    permission_required = "products.change_product"
    success_url = "/products/"


class ProductDeleteView(BaseDeleteView):
    model = Product
    template_name = "products/products-delete.html"
    permission_required = "products.delete_product"
    success_url = "/products/"

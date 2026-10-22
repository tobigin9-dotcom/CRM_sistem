from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from core.views import logout_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    # Existing _base.html uses a GET link for logout; keep the supplied template unchanged.
    path("accounts/logout", logout_view, name="logout"),
    path("accounts/logout/", logout_view),
    path("", include("core.urls")),
    path("products/", include("products.urls")),
    path("ads/", include("advertisements.urls")),
    path("leads/", include("leads.urls")),
    path("contracts/", include("contracts.urls")),
    path("customers/", include("customers.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

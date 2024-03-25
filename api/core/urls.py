from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("properties.urls", namespace="properties")),
    path("api/auth/", include("user.urls", namespace="user")),
]

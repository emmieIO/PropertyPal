# tenants/urls.py 
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import TenantViewSet

router = DefaultRouter()
router.register(r'tenants', TenantViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    # path('api/documentation/', views.api_documentation, name='api_documentation'),
    path('tenants/', views.tenant_list, name='tenants'),
]


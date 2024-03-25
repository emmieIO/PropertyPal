# urls.py in the 'tenants' app
from django.urls import path
from . import views


urlpatterns = [
    path('api/tenants/', views.TenantListCreate.as_view(), name='tenant-list-create'),
    path('api/tenants/<int:pk>/', views.TenantRetrieveUpdateDestroy.as_view(), name='tenant-detail'),
    path('tenants/', views.tenant_list, name='tenants'),
]


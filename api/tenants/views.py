# tenants/views.py
from django.shortcuts import render
from rest_framework import viewsets
from .models import Tenant
from .serializers import TenantSerializer


class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

def api_documentation(request):
    tenants = Tenant.objects.all()
    context = {
        'tenants': tenants,
    }
    return render(request, 'tenants/api.html', context)

def tenant_list(request):
    get_all_tenants = Tenant.objects.all()
    context = {
    	'display_tenants': get_all_tenants,
    }
    return render(request, 'tenants/tenant_list.html', context)

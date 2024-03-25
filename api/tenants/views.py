# views.py in the 'tenants' app
from django.shortcuts import render
# Create views using DRF's generic views
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Tenant
from .serializers import TenantSerializer

class TenantListCreate(generics.ListCreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [IsAuthenticated]

class TenantRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [IsAuthenticated]


def tenant_list(request):
    get_all_tenants = Tenant.objects.all()
    context = {
    	'display_tenants': get_all_tenants,
    }
    return render(request, 'tenants/tenant_list.html', context)

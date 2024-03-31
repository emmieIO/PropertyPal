from django.urls import path
from .views import get_landlords, landlord_login

app_name = "user"

urlpatterns = [path("landlord/", get_landlords), path("landlord/login", landlord_login)]

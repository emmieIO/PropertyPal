from django.contrib import admin
from .models import User, Landlord, LandlordProfile
from rest_framework.authtoken.admin import TokenAdmin

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    search_fields = ["username", "email"]


admin.site.register(User, UserAdmin)
admin.site.register(Landlord)
admin.site.register(LandlordProfile)

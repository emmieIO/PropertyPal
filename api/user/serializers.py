from rest_framework import serializers
from .models import LandlordProfile, Landlord


class LandLordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landlord
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        )


class LandlordProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandlordProfile
        fields = "__all__"

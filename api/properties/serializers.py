from rest_framework import serializers
from .models import Property as House
from .models import PropertyType


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        # fields = "__all__"
        exclude = ("owner",)


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = "__all__"

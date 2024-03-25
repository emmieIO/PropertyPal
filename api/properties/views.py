from django.shortcuts import render
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import status
from rest_framework.response import Response
from .serializers import PropertySerializer, PropertyTypeSerializer
from .models import Property, PropertyType


@api_view(["GET"])
def all_properties(request):
    queryset = Property.objects.all()
    serializer = PropertySerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def property_create(request):
    if request.method == "POST":
        user = request.user
        if user.role == "ADMIN" or user.role == "LANDLORD":
            serializer = PropertySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(owner=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(
                {
                    "error": "Unauthorized. Only ADMIN or LANDLORD can create properties."
                },
                status=status.HTTP_403_FORBIDDEN,
            )


@api_view(["PUT"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def property_update(request, property_id):
    if request.method == "PUT":
        try:
            property_instance = Property.objects.get(id=property_id)
        except Property.DoesNotExist:
            return Response(
                {"error": "Property not found"}, status=status.HTTP_404_NOT_FOUND
            )
        if request.user != property_instance.owner:
            return Response(
                {"error": "You are not the owner of this property"},
                status=status.HTTP_403_FORBIDDEN,
            )
        user = request.user
        if user.role == "ADMIN" or user.role == "LANDLORD":
            serializer = PropertySerializer(property_instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(
                {
                    "error": "Unauthorized. Only ADMIN or LANDLORD can create properties."
                },
                status=status.HTTP_403_FORBIDDEN,
            )


@api_view(["DELETE"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def property_delete(request, property_id):
    if request.method == "DELETE":
        try:
            property_instance = Property.objects.get(id=property_id)
        except Property.DoesNotExist:
            return Response(
                {"error": "Property not found"}, status=status.HTTP_404_NOT_FOUND
            )
        if request.user != property_instance.owner:
            return Response(
                {"error": "You are not the owner of this property"},
                status=status.HTTP_403_FORBIDDEN,
            )
        property_instance.delete()
        return Response(
            {"success": "Property Deleted."}, status=status.HTTP_204_NO_CONTENT
        )


@api_view(["POST"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def property_create_type(request):
    if request.method == "POST":
        user = request.user
        if user.role == "ADMIN":
            serializer = PropertyTypeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {"error": "Unauthorized. Only ADMIN can create property type"},
                status=status.HTTP_403_FORBIDDEN,
            )


@api_view(["PUT"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def property_update_type(request, type_id):
    if request.method == "PUT":
        try:
            type_instance = PropertyType.objects.get(id=type_id)
        except PropertyType.DoesNotExist:
            return Response(
                {"error": "Property type not found"}, status=status.HTTP_404_NOT_FOUND
            )

        user = request.user
        if user.role == "ADMIN":
            serializer = PropertyTypeSerializer(type_instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {"error": "Unauthorized. Only ADMIN can create property type"},
                status=status.HTTP_403_FORBIDDEN,
            )


@api_view(["DELETE"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def property_type_delete(request, type_id):
    if request.method == "DELETE":
        try:
            type_instance = PropertyType.objects.get(id=type_id)
        except PropertyType.DoesNotExist:
            return Response(
                {"error": "Property type not found"}, status=status.HTTP_404_NOT_FOUND
            )
        if request.user.role != "ADMIN":
            return Response(
                {"error": "You are not authorized to delete this field"},
                status=status.HTTP_403_FORBIDDEN,
            )
        type_instance.delete()
        return Response(
            {"success": "Property type Deleted."}, status=status.HTTP_204_NO_CONTENT
        )

from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.response import Response
from .models import LandlordProfile, User, Landlord
from .serializers import LandlordProfileSerializer, LandLordSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .permissions import AdminOnlyView, AdminLandlordOnlyView
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from .token_utils import create_token

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated, AdminOnlyView])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def get_landlords(request):
    if request.method == "GET":
        queryset = Landlord.landlord.all()
        serializer = LandLordSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated, AdminOnlyView])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def register_landlords(request):
    serializer = LandLordSerializer(data=request.data)
    if serializer.is_valid():
        # Create a new Landlord object
        new_landlord = Landlord.objects.create(
            username=serializer.validated_data["username"],
            email=serializer.validated_data["email"],
            first_name=serializer.validated_data["first_name"],
            last_name=serializer.validated_data["last_name"],
        )
        # Set password using set_password method
        password = serializer.validated_data.get("password")
        if password:
            new_landlord.set_password(password)
            new_landlord.save()

        # Create user Authorization token
        token = create_token(user=new_landlord)

        # Serialize the new Landlord object
        serialized_landlord = LandLordSerializer(new_landlord)
        response_data = {
            "landlord": serialized_landlord.data,
            "token": token.key,  # Include the token in the response
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([IsAuthenticated, AdminLandlordOnlyView])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def update_landlordProfile(request, pk):
    try:
        landlord = Landlord.landlord.get(pk=pk)
    except Landlord.DoesNotExist:
        return Response({"error": "Landlord not found"}, status=404)

    if request.method == "PUT":
        req = request

        if req.user.role != "ADMIN" and req.user.role != "LANDLORD":
            return Response({"error": "Authorization Failed"}, status=403)

        serializer = LandLordSerializer(landlord, data=request.data, partial=True)
        # Check if 'password' field is present in the request data
        
        if serializer.is_valid():
            password = serializer.validated_data['password']
            hashed_password = make_password(password)
            serializer.save(password = hashed_password)
            return Response(serializer.data)
        return Response({"error": "Bad Request"}, status=400)


@api_view(["POST"])
def landlord_login(request):
    if request.method == "POST":
        username = request.data["username"]
        password = request.data["password"]

        # Authenticate Landlord
        user = authenticate(username=username, password=password)

        if user is not None and user.role == "LANDLORD":
            Token.objects.filter(user=user).delete()
            token = create_token(user=user)
            landlord = Landlord.objects.get(username=request.data["username"])
            serializer = LandLordSerializer(landlord)
            print(serializer.data)
            return Response(
                {"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

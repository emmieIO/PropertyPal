from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import LandlordProfile, User, Landlord
from .serializers import LandlordProfileSerializer, LandLordSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import AdminOnlyView
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


@api_view(["GET", "POST"])
# @permission_classes([IsAuthenticated, AdminOnlyView])
def get_landlords(request):
    if request.method == "GET":
        queryset = Landlord.landlord.all()
        serializer = LandLordSerializer(queryset, many=True)
        return Response(serializer.data)

    serializer = LandLordSerializer(data=request.data)
    if serializer.is_valid():
        # Create a new Landlord object
        new_landlord = Landlord.objects.create(
            username=serializer.validated_data["username"],
            email=serializer.validated_data["email"],
        )
        # Set password using set_password method
        password = serializer.validated_data.get("password")
        if password:
            new_landlord.set_password(password)
            new_landlord.save()

        # Create user Authorization token
        token = Token.objects.create(user=new_landlord)

        # Serialize the new Landlord object
        serialized_landlord = LandLordSerializer(new_landlord)
        response_data = {
            "landlord": serialized_landlord.data,
            "token": token.key,  # Include the token in the response
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def landlord_login(request):
    if request.method == "POST":
        username = request.data["username"]
        password = request.data["password"]

        # Authenticate Landlord
        user = authenticate(username=username, password=password)

        if user is not None and user.role == "LANDLORD":
            token, _ = Token.objects.get_or_create(user=user)
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

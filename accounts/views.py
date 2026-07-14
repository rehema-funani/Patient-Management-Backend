from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterSerializer


@api_view(["POST"])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({
            "message": "User registered successfully",
            "success": True,
            "code": 201,
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    return Response({
        "message": serializer.errors,
        "success": False,
        "code": 400
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user:
        return Response({
            "message": "Login successful",
            "success": True,
            "code": 200,
            "data": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        })

    return Response({
        "message": "Invalid credentials",
        "success": False,
        "code": 401
    }, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["GET"])
def profile(request):
    return Response({
        "message": "Profile endpoint",
        "success": True,
        "code": 200
    })
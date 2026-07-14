from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Vital
from .serializers import VitalSerializer


# CREATE
@api_view(["POST"])
def create_vital(request):

    serializer = VitalSerializer(data=request.data)

    if serializer.is_valid():
        vital = serializer.save()

        return Response(
            {
                "message": "Vital recorded successfully",
                "success": True,
                "code": 201,
                "data": VitalSerializer(vital).data,
            },
            status=status.HTTP_201_CREATED,
        )

    return Response(
        {
            "message": serializer.errors,
            "success": False,
            "code": 400,
        },
        status=status.HTTP_400_BAD_REQUEST,
    )


# LIST
@api_view(["GET"])
def list_vitals(request):

    vitals = Vital.objects.all().order_by("-id")

    serializer = VitalSerializer(vitals, many=True)

    return Response(
        {
            "message": "success",
            "success": True,
            "code": 200,
            "data": serializer.data,
        }
    )


# GET ONE
@api_view(["GET"])
def get_vital(request, pk):

    try:
        vital = Vital.objects.get(id=pk)

    except Vital.DoesNotExist:
        return Response(
            {
                "message": "Vital not found",
                "success": False,
                "code": 404,
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    serializer = VitalSerializer(vital)

    return Response(
        {
            "message": "success",
            "success": True,
            "code": 200,
            "data": serializer.data,
        }
    )


# UPDATE
@api_view(["PUT"])
def update_vital(request, pk):

    try:
        vital = Vital.objects.get(id=pk)

    except Vital.DoesNotExist:
        return Response(
            {
                "message": "Vital not found",
                "success": False,
                "code": 404,
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    serializer = VitalSerializer(vital, data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(
            {
                "message": "Vital updated successfully",
                "success": True,
                "code": 200,
                "data": serializer.data,
            }
        )

    return Response(
        {
            "message": serializer.errors,
            "success": False,
            "code": 400,
        },
        status=status.HTTP_400_BAD_REQUEST,
    )


# DELETE
@api_view(["DELETE"])
def delete_vital(request, pk):

    try:
        vital = Vital.objects.get(id=pk)

    except Vital.DoesNotExist:
        return Response(
            {
                "message": "Vital not found",
                "success": False,
                "code": 404,
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    vital.delete()

    return Response(
        {
            "message": "Vital deleted successfully",
            "success": True,
            "code": 200,
        }
    )
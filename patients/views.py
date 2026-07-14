from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Patient
from .serializers import PatientSerializer


# CREATE
@api_view(["POST"])
def create_patient(request):

    serializer = PatientSerializer(data=request.data)

    if serializer.is_valid():
        patient = serializer.save()

        return Response(
            {
                "message": "Patient created successfully",
                "success": True,
                "code": 201,
                "data": PatientSerializer(patient).data,
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
def list_patients(request):

    patients = Patient.objects.all().order_by("-id")

    serializer = PatientSerializer(patients, many=True)

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
def get_patient(request, pk):

    try:
        patient = Patient.objects.get(id=pk)

    except Patient.DoesNotExist:
        return Response(
            {
                "message": "Patient not found",
                "success": False,
                "code": 404,
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    serializer = PatientSerializer(patient)

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
def update_patient(request, pk):

    try:
        patient = Patient.objects.get(id=pk)

    except Patient.DoesNotExist:
        return Response(
            {
                "message": "Patient not found",
                "success": False,
                "code": 404,
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    serializer = PatientSerializer(patient, data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(
            {
                "message": "Patient updated successfully",
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
def delete_patient(request, pk):

    try:
        patient = Patient.objects.get(id=pk)

    except Patient.DoesNotExist:
        return Response(
            {
                "message": "Patient not found",
                "success": False,
                "code": 404,
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    patient.delete()

    return Response(
        {
            "message": "Patient deleted successfully",
            "success": True,
            "code": 200,
        }
    )
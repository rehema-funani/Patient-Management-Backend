from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Visit
from .serializers import VisitSerializer


@api_view(["POST"])
def create_visit(request):

    serializer = VisitSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({
            "message": "Visit created successfully",
            "success": True,
            "code": 201,
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    return Response({
        "message": serializer.errors,
        "success": False,
        "code": 400
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def list_visits(request):

    visits = Visit.objects.all().order_by("-id")

    serializer = VisitSerializer(visits, many=True)

    return Response({
        "message": "success",
        "success": True,
        "code": 200,
        "data": serializer.data
    })


@api_view(["GET"])
def get_visit(request, pk):

    try:
        visit = Visit.objects.get(id=pk)

    except Visit.DoesNotExist:
        return Response({
            "message": "Visit not found",
            "success": False,
            "code": 404
        }, status=status.HTTP_404_NOT_FOUND)

    serializer = VisitSerializer(visit)

    return Response({
        "message": "success",
        "success": True,
        "code": 200,
        "data": serializer.data
    })


@api_view(["PUT"])
def update_visit(request, pk):

    try:
        visit = Visit.objects.get(id=pk)

    except Visit.DoesNotExist:
        return Response({
            "message": "Visit not found",
            "success": False,
            "code": 404
        }, status=status.HTTP_404_NOT_FOUND)

    serializer = VisitSerializer(
        visit,
        data=request.data
    )

    if serializer.is_valid():
        serializer.save()

        return Response({
            "message": "Visit updated successfully",
            "success": True,
            "code": 200,
            "data": serializer.data
        })

    return Response({
        "message": serializer.errors,
        "success": False,
        "code": 400
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_visit(request, pk):

    try:
        visit = Visit.objects.get(id=pk)

    except Visit.DoesNotExist:
        return Response({
            "message": "Visit not found",
            "success": False,
            "code": 404
        }, status=status.HTTP_404_NOT_FOUND)

    visit.delete()

    return Response({
        "message": "Visit deleted successfully",
        "success": True,
        "code": 200
    })
from rest_framework import serializers
from .models import Vital


class VitalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vital
        fields = "__all__"
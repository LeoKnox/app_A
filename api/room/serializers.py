from .models import Room
from django.core import serializers as core_serializers
from rest_framework import serializers

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        field = (
            "name", "description", "length", "width"
        )
        fields = '__all__'
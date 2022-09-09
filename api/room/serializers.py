from .models import Room
from rest_framework import serializers

class RoomSerializer(serializers.Serializer):
    class Meta:
        model = Room
        field = {
            "name", "description"
        }
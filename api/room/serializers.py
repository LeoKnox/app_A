from .models import Room
from rest_framework import serializers

class RoomSerializer(serializers.HyperLinkModelSerializer):
    class Meta:
        model = Room
        field = (
            "name", "description", "length", "width"
        )
        fields = '__all__'
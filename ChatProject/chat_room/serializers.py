from rest_framework import serializers

from .models import User, Room, Chat


class RoomSerializers(serializers.ModelSerializer):
    """serializers chat room"""

    class Meta:
        model = Room
        fields = ('creator', 'invited', 'date')


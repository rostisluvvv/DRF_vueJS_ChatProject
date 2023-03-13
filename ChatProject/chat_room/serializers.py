from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Room, Chat


class UserSerializers(serializers.ModelSerializer):
    """Serialization Users."""

    class Meta:
        model = User
        fields = ('id', 'username')


class RoomSerializers(serializers.ModelSerializer):
    """Serialization chat room."""

    creator = UserSerializers()
    invited = UserSerializers(many=True)

    class Meta:
        model = Room
        fields = ('creator', 'invited', 'date')


class ChatSerializers(serializers.ModelSerializer):
    """Serialization Chat."""
    user = UserSerializers()
    class Meta:
        model = Chat
        fields = ('room', 'user', 'text', 'date')


class ChatPostSerializers(serializers.ModelSerializer):
    """Serialization Chat."""
    class Meta:
        model = Chat
        fields = ('text', 'room')

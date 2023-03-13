from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import Room, Chat
from .serializers import (RoomSerializers,
                          ChatSerializers,
                          ChatPostSerializers)


class Rooms(APIView):

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializers(rooms, many=True)
        return Response({'data': serializer.data})


class Dialog(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        room = request.GET.get('room')
        chats = Chat.objects.filter(room=room)
        serializer = ChatSerializers(chats, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        dialog = ChatPostSerializers(data=request.data)

        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response({'status': 'Add'})

        else:
            return Response({'status': 'Error'})


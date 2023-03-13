from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import Room
from .serializers import RoomSerializers


class Rooms(APIView):

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializers(rooms, many=True)
        return Response(serializer.data)



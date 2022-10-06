from rest_framework import viewsets,permissions

from apps.rooms.models import Rooms
from apps.rooms.serializers import RoomsSerializers


class RoomsApiViewset(viewsets.ModelViewSet):
    queryset=Rooms.objects.all()
    serializer_class=RoomsSerializers
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

from rest_framework import viewsets,permissions,filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.rooms.models import Rooms
from apps.rooms.serializers import RoomsSerializers


class RoomsApiViewset(viewsets.ModelViewSet):
    queryset=Rooms.objects.all()
    serializer_class=RoomsSerializers
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['room_number', 'room']

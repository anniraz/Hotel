from rest_framework import viewsets,permissions

from apps.restaurant.models import Restuarant,Menu
from apps.restaurant.serializers import RestuarantSerializers,MenuSerilizers
# Create your views here.

class RestuarantApiViewset(viewsets.ModelViewSet):
    queryset=Restuarant.objects.all()
    serializer_class=RestuarantSerializers
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]


class MenuApiViewset(viewsets.ModelViewSet):
    queryset=Menu.objects.all()
    serializer_class=MenuSerilizers
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

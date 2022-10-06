from rest_framework import viewsets,permissions

from apps.clubs.models import ClubsInfo,Clubs,SpaEtiquette
from apps.clubs.serializers import *

class ClubsInfoApiViewset(viewsets.ModelViewSet):
    queryset=ClubsInfo.objects.all()
    serializer_class=ClubsInfoSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

class ClubsApiViewset(viewsets.ModelViewSet):
    queryset=Clubs.objects.all()
    serializer_class=ClubsSerializers
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

class ClubsEtiquetteApiViewset(viewsets.ModelViewSet):
    queryset=SpaEtiquette.objects.all()
    serializer_class=ClubsEtiquetteSerializers
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

from rest_framework import serializers
 
from apps.clubs.models import *


class ClubsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClubsInfo
        fields='__all__'


class ClubsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Clubs
        fields='__all__'

class ClubsEtiquetteSerializers(serializers.ModelSerializer):
    class Meta:
        model=SpaEtiquette
        fields='__all__'
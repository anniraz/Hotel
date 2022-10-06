from rest_framework import serializers

from apps.restaurant.models import *

class RestuarantSerializers(serializers.ModelSerializer):
    class Meta:
        model=Restuarant
        fields='__all__'

class MenuSerilizers(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields='__all__'
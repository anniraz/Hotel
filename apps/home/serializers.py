from rest_framework import serializers
 
from apps.home.models import *


class PhotoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model=PhotoGallery
        fields='__all__'

class VideoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model=VideoGallery
        fields='__all__'

class AboutHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model=AboutHotel
        fields='__all__'
    

class HotelFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model=HotelFacilities
        fields='__all__'


class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=OurTeam
        fields='__all__' 

class ExtraServicesInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=ExtraServicesInfo
        fields='__all__'
    
class ExtraServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model=ExtraServices
        fields='__all__'


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactUs
        fields='__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reviews
        fields='__all__'
from rest_framework import viewsets,permissions
# Create your views here.
from apps.home.models import *
from apps.home.serializers import *



class AboutHotelApiViewset(viewsets.ModelViewSet):
    queryset=AboutHotel.objects.all()
    serializer_class=AboutHotelSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

class HotelFacilitiesApiViewset(viewsets.ModelViewSet):
    queryset=HotelFacilities.objects.all()
    serializer_class=HotelFacilitiesSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]


class OurTeamApiViewset(viewsets.ModelViewSet):
    queryset=OurTeam.objects.all()
    serializer_class=OurTeamSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

class ExtraServicesInfoApiViewset(viewsets.ModelViewSet):
    queryset=ExtraServicesInfo.objects.all()
    serializer_class=ExtraServicesInfoSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]


class ExtraServicesApiViewset(viewsets.ModelViewSet):
    queryset=ExtraServices.objects.all()
    serializer_class=ExtraServicesSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]


class ContactUsApiViewset(viewsets.ModelViewSet):
    queryset=ContactUs.objects.all()
    serializer_class=ContactUsSerializer

class ReviewsApiViewset(viewsets.ModelViewSet):
    queryset=Reviews.objects.all()
    serializer_class=ReviewsSerializer

class PhotoGalleryApiViewset(viewsets.ModelViewSet):
    queryset=PhotoGallery.objects.all()
    serializer_class=PhotoGallerySerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

class VideoGalleryApiViewset(viewsets.ModelViewSet):
    queryset=VideoGallery.objects.all()
    serializer_class=VideoGallerySerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
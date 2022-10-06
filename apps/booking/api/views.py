from rest_framework import viewsets

from apps.booking.models import HotelBooking
from apps.booking.serializers import BookingSerializer

class BookingApiView(viewsets.ModelViewSet):
    queryset=HotelBooking.objects.all()
    serializer_class=BookingSerializer

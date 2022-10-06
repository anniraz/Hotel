from rest_framework import serializers


from apps.booking.models import HotelBooking

from apps.booking.tasks import send_to_email


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelBooking
        fields='__all__'    
    
    def create(self,validated_data):
        booking = super().create(validated_data)
        full_name = validated_data['full_name']
        check_in = validated_data['check_in']
        check_out = validated_data['check_out']
        email = validated_data['email']
        room = validated_data['room']
        
        dates=check_out-check_in
        days=0
        for d in range(dates.days):
            days+=1
        total_price=room.price*days
        send_to_email.delay(email,full_name,room.room,check_in,check_out,total_price,room.room_number)
        return booking
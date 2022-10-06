import datetime
from hotel.celery import app

from django.core.mail import send_mail

from apps.booking.models import HotelBooking
from apps.rooms.models import Rooms




@app.task
def check_time():
    d=HotelBooking.objects.filter(check_out__lte=datetime.datetime.now().date())

    if d:
        for i in d:
            id=i.room.id
            room=Rooms.objects.get(id=id)
            room.is_available=True
            room.save()
            send_mail(
                    f'Hello,{i.full_name} ',
                    f'{i.room.room} №{i.room.room_number}: your booking time out :) ',
                    'zarinakudajberdikyzy@gmail.com',
                    [i.email],
                    fail_silently=False,
            )
        d.delete()
        print('DELETED')
    else:
        print('NOT DELETED')


@app.task
def send_to_email(email,name,room,time1,time2,price,room_number):
    send_mail(
        f'Hello,{name} ',
        f'You  have booked a {room} room from {time1} to {time2}\n total price-{price} \nYour room number is {room_number}\n Have a good time :) ',
        'zarinakudajberdikyzy@gmail.com',
        [email],
        fail_silently=False,
            )
    


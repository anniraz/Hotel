import datetime
from django.shortcuts import render,redirect
from apps.booking.models import HotelBooking
from apps.home.models import AboutHotel,ExtraServices,ExtraServicesInfo
from apps.rooms.models import Rooms

from apps.booking.tasks import send_to_email


def booking(request,id):
        roomss=Rooms.objects.get(id=id)
        if request.method == 'POST':
            form=HotelBooking()
            name=request.POST.get('full_name')
            email=request.POST.get('email')
            check_in=request.POST.get('check_in')
            check_out=request.POST.get('check_out')
            adults=request.POST.get('adults')
            children=request.POST.get('children')
            
            
            form.full_name=name 
            form.check_in=datetime.datetime.strptime(check_in, "%m/%d/%Y").date()
            form.check_out=datetime.datetime.strptime(check_out, "%m/%d/%Y").date()   
            form.adults=adults
            form.children=children
            form.room=roomss
            form.email=email
            roomss.is_available=False
            roomss.save()

            form.save()
    
            dates=form.check_out-form.check_in
            days=0
            for d in range(dates.days):
                days+=1
            total_price=roomss.price*days
            send_to_email.delay(email,name,roomss.room,check_in,check_out,total_price,roomss.room_number)
            return redirect('home' )
        else:
            about=AboutHotel.objects.latest('id')
            service=ExtraServices.objects.all()
            service_info=ExtraServicesInfo.objects.latest('id')
            context={
                    'about':about,
                    'all_rooms':roomss,
                    'service':service,
                    'service_info':service_info,
                    
                                }
            return render(request, 'reservation.html', context)
            


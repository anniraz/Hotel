import datetime
from django.shortcuts import render
from django.db.models import Q

from apps.home.models import AboutHotel, ExtraServices, ExtraServicesInfo,HotelFacilities
from apps.rooms.models import Rooms
from apps.booking.models import HotelBooking


def rooms(request):
    if 'search_button' in request.GET:
        search_check_in=request.GET.get('check_in')
        search_check_out=request.GET.get('check_out')
        search_adults=request.GET.get('adults')
        search_children=request.GET.get('children')
        check_in=datetime.datetime.strptime(search_check_in, "%m/%d/%Y").date()
        check_out=datetime.datetime.strptime(search_check_out, "%m/%d/%Y").date()
        rooms=HotelBooking.objects.all()
       
        if rooms is not None:
            l=[]
            for i in rooms:
                dates=i.check_out-i.check_in
                for d in range(dates.days +1):
                    res=i.check_in+datetime.timedelta(days=d)
                    if check_in == res or check_out==res:
                        l.append(i.room.id)
                

            available_rooms=Rooms.objects.filter(Q(for_persons__icontains=search_adults,for_children__icontains=search_children,is_available=True)).exclude(id__in=l)
            about=AboutHotel.objects.latest('id')
            service=ExtraServices.objects.all()
            service_info=ExtraServicesInfo.objects.latest('id')
            context={
                'about':about,
                'all_rooms':available_rooms,
                'service':service,
                'service_info':service_info
                }
            return render(request, 'rooms.html', context)
    else:


        service_info=ExtraServicesInfo.objects.latest('id')
        about=AboutHotel.objects.latest('id')
        all_rooms=Rooms.objects.all()[3:]
        rooms3=Rooms.objects.all()[:3]
        service=ExtraServices.objects.all()
    
        context={
                'about':about,
                'all_rooms':all_rooms,
                'rooms3':rooms3,
                'service':service,
                'service_info':service_info
                        }
        return render(request,'rooms.html',context)


def roomsDetail(request,id):
    if 'search_button' in request.GET:
        search_check_in=request.GET.get('check_in')
        search_check_out=request.GET.get('check_out')
        # search_adults=request.get('adults')
        rooms=HotelBooking.objects.filter(Q(check_in__icontains=search_check_in,check_out__icontains=search_check_out))
        if rooms is not None:
            l=[]
            for i in rooms:
                l.append(i.room.id)    
            roomss=Rooms.objects.all().exclude(id__in=l)
            about=AboutHotel.objects.latest('id')
            service=ExtraServices.objects.all()
            service_info=ExtraServicesInfo.objects.latest('id')

            context={
                'all_rooms':roomss,
                'about':about,
                'service':service,
                'service_info':service_info
                }
            return render(request, 'rooms.html', context)
    
    about=AboutHotel.objects.latest('id')
    rooms=Rooms.objects.get(id=id)
    similar=Rooms.objects.all()[:6]
    facilities=HotelFacilities.objects.all()    
    service=ExtraServices.objects.all()
    service_info=ExtraServicesInfo.objects.latest('id')

    context={
        'about':about,
        'rooms':rooms,
        'facilities':facilities,
        'similar':similar,
        'service':service,
        'service_info':service_info
            }
    return render(request,'room_details.html',context)
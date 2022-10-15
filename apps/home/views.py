import datetime 

from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import  authenticate, login
from django.contrib import messages


from django.db.models import Q
from django.core.paginator import Paginator

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from apps.home.models import AboutHotel, ContactUs,HotelFacilities,OurTeam,PhotoGallery, Reviews,VideoGallery,ExtraServices,ExtraServicesInfo
from apps.restaurant.models import Restuarant
from apps.rooms.models import Rooms
from apps.clubs.models import Clubs
from apps.news.models import News
from apps.booking.models import HotelBooking
from apps.home.forms import *

def index(request):

    if 'search_button' in request.GET:
        search_check_in=request.GET.get('check_in')
        search_check_out=request.GET.get('check_out')
        search_adults=request.GET.get('adults')
        search_children=request.GET.get('children')
        search_room=request.GET.get('room')
        try:
            check_in=datetime.datetime.strptime(search_check_in, "%m/%d/%Y").date()
            check_out=datetime.datetime.strptime(search_check_out, "%m/%d/%Y").date()
        except Exception:
            return redirect('home')
        rooms=HotelBooking.objects.all()
       
        if rooms is not None:
            l=[]
            for i in rooms:
                dates=i.check_out-i.check_in
                for d in range(dates.days +1):
                    res=i.check_in+datetime.timedelta(days=d)
                    if check_in == res or check_out==res:
                        l.append(i.room.id)


            available_rooms=Rooms.objects.filter(Q(for_persons__icontains=search_adults,for_children__icontains=search_children,room_amount__icontains=search_room,is_available=True)).exclude(id__in=l)
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

        about=AboutHotel.objects.latest('id')
        facilities=HotelFacilities.objects.all()
        rooms=Rooms.objects.all()[:3]
        photo_about2=Rooms.objects.all()[3:5]
        rooms3=Rooms.objects.all()[:3]
        news=News.objects.all()[:6]
        service=ExtraServices.objects.all()
        service_info=ExtraServicesInfo.objects.latest('id')
        clubs=Clubs.objects.all()
        context={
            'about':about,
            'facilities':facilities,
            'rooms':rooms,
            'clubs':clubs,
            'news':news,
            'photo_about':photo_about2,
            'rooms3':rooms3,
            'service':service,
            'service_info':service_info
            
        }

        # class="col-md-6 p-0 animate-box" data-animate-effect="fadeInLeft"
        # class="col-md-6 p-0 bg-cream valign animate-box" data-animate-effect="fadeInRight"
        return render(request,'index.html',context)

def about(request):
    about=AboutHotel.objects.latest('id')
    facilities=HotelFacilities.objects.all()
    rooms=Rooms.objects.all()[:5]
    photo_about2=Rooms.objects.all()[3:5]
    team =OurTeam.objects.all()
    service=ExtraServices.objects.all()
    service_info=ExtraServicesInfo.objects.latest('id')
    review=Reviews.objects.filter(rating=5)[:6]
    context={
        'about':about,
        'facilities':facilities,
        'rooms':rooms,
        'photo_about':photo_about2,
        'team':team,
        'service':service,
        'service_info':service_info,
        'review':review,
        
        
    }
    return render(request,'about.html',context)

def gallery(request):
    about=AboutHotel.objects.latest('id')
    photos=PhotoGallery.objects.all()
    video=VideoGallery.objects.all()
    context={
        'photos':photos,
        'video':video,
        'about':about,

    }
    return render(request,'gallery.html',context)

def contact(request):       


    if request.method == 'POST':
            form=ContactUs()
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            message=request.POST.get('message')
            subject=request.POST.get('subject')


            try:
                validate_email(email)
            except ValidationError as e:
                print("incorrect email", e)
                return redirect('contact')
            form.name=name
            form.email=email
            form.message=message
            form.subject=subject
            form.phone=phone
            form.save()
            return redirect('contact' )


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
   
            about=AboutHotel.objects.latest('id')
            rooms=Rooms.objects.all()
            service=ExtraServices.objects.all()
            service_info=ExtraServicesInfo.objects.latest('id')
            context={
                'about':about,
                'all_rooms':rooms,
                'service':service,
                'service_info':service_info,
                }




            return render(request,'contact.html',context)

def reviews(request):
    about=AboutHotel.objects.latest('id')
    review=Reviews.objects.all()
    paginator=Paginator(review,3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form =ReviewForm()
    context={
            'about':about,
            'form': form,
            'page_obj':page_obj
            }

    return render(request,'reviews.html',context)


def admin(request):
    about=AboutHotel.objects.latest('id')
    if request.method == 'POST':
        form = AboutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admins')
    return render(request,'foradmin/hotelinform.html',locals())


def adminpage(request):
    about=AboutHotel.objects.latest('id')
    restaurant=Restuarant.objects.latest('id')
    return render(request,'foradmin.html',locals())


class HUpdate(generic.UpdateView):
    model=AboutHotel
    template_name='foradmin/hotelinform.html'
    form_class = AboutForm

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['about']=AboutHotel.objects.latest('id')
        return context


class RoomListView(generic.ListView):
    model=Rooms
    template_name='foradmin/rooms.html'
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['about']=AboutHotel.objects.latest('id')
        context['all_rooms']=Rooms.objects.all()
        return context


class RUpdateView(generic.UpdateView):
    model= Rooms
    template_name='foradmin/room_update.html'
    form_class=RoomsForm
    success_url=reverse_lazy('rooms_all')

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['about']=AboutHotel.objects.latest('id')
        return context


class PhotoGalleryUpdateView(generic.UpdateView):
    model=PhotoGallery
    template_name='foradmin/photo_gallery_update.html'
    form_class=PhotoGalleryForm
    success_url=reverse_lazy('photo_gallery')

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['about']=AboutHotel.objects.latest('id')
        return context

class PhotoGalleryDeleteView(generic.DeleteView):
    model=PhotoGallery
    template_name='foradmin/delete.html'
    success_url=reverse_lazy('photo_gallery')

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['about']=AboutHotel.objects.latest('id')
        return context

class PhotoGalleryCreateView(generic.CreateView):
    model=PhotoGallery
    template_name='foradmin/create.html'
    form_class=PhotoGalleryForm
    success_url=reverse_lazy('photo_gallery')

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['about']=AboutHotel.objects.latest('id')
        return context


class PhotoGalleryListView(generic.ListView):
    model=PhotoGallery
    template_name='foradmin/photo_gallery.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['about']=AboutHotel.objects.latest('id')
        context['photo_gallery']=PhotoGallery.objects.all()
        return context



class ContactUsListView(generic.ListView):
    model=ContactUs
    template_name='foradmin/contact.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['about']=AboutHotel.objects.latest('id')
        context['contact']=ContactUs.objects.all()
        return context

class ContactUsDeleteView(generic.DeleteView):
    model=ContactUs
    template_name='foradmin/delete.html'
    success_url=reverse_lazy('all_messages')


    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['about']=AboutHotel.objects.latest('id')
        context['contact']=ContactUs.objects.all()
        return context

def user_login_view(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('home')
            except:
                messages.error(request, 'Не правильный логин или пароль')
    form = LoginForm()
    about=AboutHotel.objects.latest('id')

    return render(request, 'foradmin/login.html', {'form': form,'about':about})



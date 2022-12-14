from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from apps.home.models import AboutHotel,Reviews
from apps.restaurant.models import *
from apps.restaurant.forms import *

def restaurant(request):
    restaurant_info=Restuarant.objects.latest('id')
    about=AboutHotel.objects.latest('id')
    category_menu=CategoryMenu.objects.all()
    menu=Menu.objects.all()[:6]
    review=Reviews.objects.filter(rating=5)[:6]
    
    context={
        'restaurant':restaurant_info,
        'about':about,
        'category_menu':category_menu,
        'menu':menu,
        'review':review
    }
    return render(request,'restaurant.html',context)

def category(request,id):
    category_menu=CategoryMenu.objects.all()
    restaurant_info=Restuarant.objects.latest('id')
    about=AboutHotel.objects.latest('id')
    menu=Menu.objects.filter(category__id=id)
    context={
        'restaurant':restaurant_info,
        'about':about,
        'category_menu':category_menu,
        'menu':menu
    }
    return render(request,'restaurant.html',context)

class RestaurantUpdateView(generic.UpdateView):
    model=Restuarant
    template_name='foradmin/restaurant.html'
    form_class=RestaurantForm
    success_url=reverse_lazy('admins')
    

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['about']=AboutHotel.objects.latest('id')
        return context



from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy


from apps.clubs.models import Clubs,ClubsInfo, SpaEtiquette
from apps.home.models import AboutHotel,Reviews

from apps.clubs.forms import *


def clubs(request):

    clubs=Clubs.objects.all()
    clubs_image=Clubs.objects.all()[:3]
    clubs_info=ClubsInfo.objects.latest('id')
    about=AboutHotel.objects.latest('id')
    etiquette=SpaEtiquette.objects.all()
    review=Reviews.objects.filter(rating=5)
    a='class="col-md-6 bg-cream p-0 order2 valign animate-box" data-animate-effect="fadeInLeft"'
    b='class="col-md-6 p-0 order1 animate-box" data-animate-effect="fadeInRight"'
 
    context={
        'clubs':clubs,
        'clubs_image':clubs_image,
        'clubs_info':clubs_info,
        'about':about,
        'etiquette':etiquette,
        'review':review
      
    }

    return render(request,'clubs.html',context)


def clubs_details(request,id):
    clubs=Clubs.objects.get(id=id)
    about=AboutHotel.objects.latest('id')
    context={
        'about':about,
        'clubs':clubs
    }
    return render(request,'clubs_detail.html',context)


class ClubsListView(generic.ListView):
    model=Clubs
    template_name='foradmin/clubs.html'
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['about']=AboutHotel.objects.latest('id')
        context['clubs']=Clubs.objects.all()
        return context

class ClubsUpdateView(generic.UpdateView):
    model=Clubs
    template_name='foradmin/club_update.html'
    form_class=ClubsForm
    success_url=reverse_lazy('clubs_all')

    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['about']=AboutHotel.objects.latest('id')
        context['clubs']=Clubs.objects.all()
        return context


class ClubsCreateView(generic.CreateView):
    model=Clubs
    template_name='foradmin/create.html'
    form_class=ClubsForm
    success_url=reverse_lazy('clubs_all')

    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['about']=AboutHotel.objects.latest('id')
        context['clubs']=Clubs.objects.all()
        return context

class ClubsDelateView(generic.DeleteView):
    model=Clubs
    template_name='foradmin/delete.html'
    success_url=reverse_lazy('clubs_all')

    # form_class=ClubsForm
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['about']=AboutHotel.objects.latest('id')
        # context['clubs']=Clubs.objects.all()
        return context
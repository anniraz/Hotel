from django.shortcuts import render

from apps.clubs.models import Clubs,ClubsInfo, SpaEtiquette
from apps.home.models import AboutHotel,Reviews



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
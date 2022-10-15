import datetime
from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy

from django.core.paginator import Paginator
from django.db.models import Q

from apps.home.models import AboutHotel,ExtraServices,ExtraServicesInfo
from apps.news.models import News,NewsCategory,Comments
from apps.booking.models import HotelBooking
from apps.rooms.models import Rooms
from .forms import *

def news(request):

    if 'search' in request.GET:
        word = request.GET.get('search_word')
        page_obj = News.objects.filter(Q(title__icontains=word))
        about=AboutHotel.objects.latest('id')
        return render(request, 'news.html', {'page_obj': page_obj,'about':about})

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
        news=News.objects.all()
        paginator=Paginator(news,6)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        context={
            'about':about,
            'news':news,
            'page_obj':page_obj
        }
        return render(request,'news.html',context)


def post(request,id):
    if 'search_button' in request.GET:
        word = request.GET.get('search_word')
        page_obj = News.objects.filter(Q(title__icontains=word))
        about=AboutHotel.objects.latest('id')
        return render(request, 'news.html', {'page_obj': page_obj,'about':about})
    else:
        about=AboutHotel.objects.latest('id')
        news=News.objects.get(id=id)
        resent_post=News.objects.all().order_by('-id')[:3]
        categories=NewsCategory.objects.all()
        review=Comments.objects.filter(news_id=news)
        paginator=Paginator(review,4)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)


        
        if request.method == 'POST':
            form=Comments()
            full_name=request.POST.get('name')
            email=request.POST.get('email')
            text=request.POST.get('message')
            form.full_name=full_name
            form.email=email
            form.text=text
            form.news=news
            form.save()
            return redirect('detail_post' ,news.id )
        else:
            form=Comments()

        context={
            'about':about,
            'news':news,
            'resent_post':resent_post,
            'categories':categories,
            'review':review,
            'form':form,
            'page_obj':page_obj
        }
        return render(request,'post.html',context)

def reply(request,id,id1):
    news=News.objects.get(id=id)
    about=AboutHotel.objects.latest('id')
    resent_post=News.objects.all().order_by('-id')[:3]
    categories=NewsCategory.objects.all()
    review=Comments.objects.filter(news_id=news)
    paginator=Paginator(review,3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    if request.method == 'POST':
        form=Comments()
        full_name=request.POST.get('name')
        email=request.POST.get('email')
        text=request.POST.get('message')
        form.full_name=full_name
        form.email=email
        form.text=text
        form.news=news
        form.parent=Comments.objects.get(id=id1)
        form.save()
        return redirect('detail_post' ,news.id)
    else:
        form=Comments()
    context={
            'about':about,
            'news':news,
            'resent_post':resent_post,
            'categories':categories,
            'review':review,
            'form':form,
            'page_obj':page_obj,
            'parent':Comments.objects.get(id=id1)
        }
    return render(request,'post.html',context)


def categoryPost(request,id):

    news=News.objects.filter(category__id=id)
    about=AboutHotel.objects.latest('id')
    paginator=Paginator(news,6)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={
        'about':about,
        'news':news,
        'page_obj':page_obj
    }
    return render(request,'news.html',context)

class NewsUpdateView(generic.UpdateView):
    model= News
    template_name='foradmin/news_update.html'
    form_class=NewsForm
    success_url=reverse_lazy('news_all')
    

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['about']=AboutHotel.objects.latest('id')
        return context


class NewsDeleteView(generic.DeleteView):
    model= News
    template_name='foradmin/delete.html'
    # form_class=NewsForm
    success_url=reverse_lazy('news_all')
    

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['about']=AboutHotel.objects.latest('id')
        return context


class NewsCreateView(generic.CreateView):
    model= News
    template_name='foradmin/create.html'
    form_class=NewsForm
    success_url=reverse_lazy('news_all')
    

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['about']=AboutHotel.objects.latest('id')
        return context


class AdminNewsListView(generic.ListView):
    model=News
    template_name='foradmin/news.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['about']=AboutHotel.objects.latest('id')
        context['news']=News.objects.all()
        return context


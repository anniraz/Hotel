from django.urls import path

from apps.home.views import index,about,gallery,contact,reviews,admin,HUpdate



urlpatterns=[

    path('',index,name='home'),
    path('about/',about,name='about'),
    path('gallery/',gallery,name='gallery'),
    path('contact/',contact,name='contact'),
    path('review/',reviews, name='reviews'),
    # path('admins/',admin, name='admins'),
    # path('update/<int:pk>/',HUpdate.as_view(), name='update'),


]

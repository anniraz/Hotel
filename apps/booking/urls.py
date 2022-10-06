from django.urls import path

from apps.booking.views import booking



urlpatterns=[
    path('booking/<int:id>/',booking,name='reservation'),


]

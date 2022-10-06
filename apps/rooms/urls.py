from django.urls import path

from apps.rooms.views import rooms,roomsDetail


urlpatterns=[
    path('rooms/',rooms,name='rooms'),
    path('rooms/<int:id>/',roomsDetail,name='room_detail')




]




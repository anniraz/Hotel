from django.urls import path

from apps.clubs.views import *


urlpatterns=[
    path('clubs/',clubs,name='clubs'),
    path('clubs/<int:id>/',clubs_details,name='clubs_details'),
    path('admins/clubs/',ClubsListView.as_view(),name='clubs_all'),
    path('admins/clubs/update/<int:pk>/',ClubsUpdateView.as_view(),name='club_update'),
    path('admins/clubs/delete/<int:pk>/',ClubsDelateView.as_view(),name='club_delete'),
    path('admins/clubs/create/',ClubsCreateView.as_view(),name='club_create'),
    


]

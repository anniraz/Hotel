from django.urls import path
from django.contrib.auth.views import LogoutView

from apps.home.views import *



urlpatterns=[

    path('',index,name='home'),
    path('about/',about,name='about'),
    path('gallery/',gallery,name='gallery'),
    path('contact/',contact,name='contact'),
    path('review/',reviews, name='reviews'),

    path('admins/',adminpage, name='admins'),
    path('admins/login/',user_login_view,name='admins_login'),
    path('admins/logout/', LogoutView.as_view(next_page='home'), name='admins_logout'),
    path('admins/update/<int:pk>/',HUpdate.as_view(), name='update'),
    path('admins/rooms/',RoomListView.as_view(), name='rooms_all'),
    path('admins/room/<int:pk>/',RUpdateView.as_view(), name='room_update'),
    path('admins/photo_gallery/',PhotoGalleryListView.as_view(),name='photo_gallery'),
    path('admins/photo_gallery/update/<int:pk>/',PhotoGalleryUpdateView.as_view(),name='photo_gallery_update'),
    path('admins/photo_gallery/delete/<int:pk>/', PhotoGalleryDeleteView.as_view(),name='photo_delete'),
    path('admins/photo_gallery/create/', PhotoGalleryCreateView.as_view(),name='photo_create'),
    path('admins/contact/',ContactUsListView.as_view(),name='all_messages'),
    path('admins/contact/delete/<int:pk>/', ContactUsDeleteView.as_view(),name='contact_delete'),

]

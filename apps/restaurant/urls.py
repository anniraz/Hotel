from django.urls import path
from apps.restaurant.views import *



urlpatterns=[

    path('restaurant/',restaurant,name='restaurant'),
    path('menu/<int:id>/',category,name='category'),
    path('admins/restaurant/<int:pk>/',RestaurantUpdateView.as_view(),name='restaurant_update')


]

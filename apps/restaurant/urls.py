from django.urls import path
from apps.restaurant.views import restaurant,category



urlpatterns=[

    path('restaurant/',restaurant,name='restaurant'),
    path('menu/<int:id>/',category,name='category')


]

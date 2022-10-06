from django.urls import path

from apps.clubs.views import clubs,clubs_details


urlpatterns=[
    path('clubs/',clubs,name='clubs'),
    path('clubs/<int:id>/',clubs_details,name='clubs_details')
    


]

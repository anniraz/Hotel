from django.urls import path

from apps.booking.views import booking,HBookingListView,HBookingDeleteView



urlpatterns=[
    path('booking/<int:id>/',booking,name='reservation'),
    path('admins/books/',HBookingListView.as_view(),name='booked_list'),
    path('admins/reservation/delete/<int:pk>/',HBookingDeleteView.as_view(),name='delete_booking')


]

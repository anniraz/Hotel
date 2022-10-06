from django import forms

from .models import *

class BookingForm(forms.ModelForm):
    class Meta:
        model=HotelBooking
        fields=['full_name','email','check_in','check_out','adults','children','room']

        widgets = {

            'full_name': forms.TextInput(attrs={'class': 'input1_inner'}),
            'email': forms.EmailInput(attrs={'class': 'input1_inner'}),
            'check_in': forms.TextInput(attrs={'class': 'form-control input datepicker'}),
            'check_out': forms.TextInput(attrs={'class': 'form-control input datepicker'}),
            'adults': forms.TextInput(attrs={'class': 'select1_inner'}),
            'children': forms.TextInput(attrs={'class': 'select_inner'}),

        }
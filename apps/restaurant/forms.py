from django import forms

from apps.rooms.models import Rooms
from .models import *


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restuarant
        fields = '__all__'

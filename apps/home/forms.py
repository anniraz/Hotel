from django import forms


from apps.rooms.models import Rooms
from .models import *


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ["full_name","email","rating","text"]

class AboutForm(forms.ModelForm):
    class Meta:
        model=AboutHotel
        fields='__all__'

class RoomsForm(forms.ModelForm):
    class Meta:
        model=Rooms
        fields='__all__'

class PhotoGalleryForm(forms.ModelForm):
    class Meta:
        model=PhotoGallery
        fields='__all__'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
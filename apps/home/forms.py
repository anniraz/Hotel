from django import forms
from .models import *


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ["full_name","email","rating","text"]

class AboutForm(forms.ModelForm):
    class Meta:
        model=AboutHotel
        fields='__all__'

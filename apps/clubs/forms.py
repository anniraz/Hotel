from django import forms

from .models import *


class ClubsForm(forms.ModelForm):
    class Meta:
        model = Clubs
        fields = '__all__'
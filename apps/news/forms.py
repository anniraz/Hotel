from django import forms

from .models import Comments, News


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'



class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
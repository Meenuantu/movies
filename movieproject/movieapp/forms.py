from django import forms
from .models import movie


class Movieform(forms.ModelForm):
    class Meta:
        model=movie
        fields=['movie_name','desc','movie_year','img']
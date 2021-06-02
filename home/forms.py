from django import forms
from django.db.models import fields
from .models import Movies


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = "__all__"

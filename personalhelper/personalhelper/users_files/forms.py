from django import forms
from django.forms import ModelForm
from .models import UserFile


class UserFileAdd(ModelForm):
    class Meta:
        model = UserFile
        fields = ['category', 'file', 'user']
        widgets = {'user': forms.HiddenInput()}

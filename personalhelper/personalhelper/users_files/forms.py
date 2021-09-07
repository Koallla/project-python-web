from django import forms
from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from .models import UserFile


class UserFileAdd(ModelForm):
    class Meta:
        model = UserFile
        fields = ['file', 'user', 'category']
        widgets = {'user': forms.HiddenInput()}

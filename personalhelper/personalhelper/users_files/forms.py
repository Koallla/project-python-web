from django import forms
from django.forms import ModelForm
from .models import UserFile


class UserFileAdd(ModelForm):
    class Meta:
        model = UserFile
        fields = ['category', 'file', 'user']
        widgets = {'user': forms.HiddenInput()}


class FilterForm(forms.Form):
    FILTER_CHOICES = (
        ('category', f'By category "\u2191"'),
        ('-category', 'By category "\u2193"'),
        ('file', 'By name "\u2191"'),
        ('-file', 'By name "\u2193"'),
    )

    order_by = forms.ChoiceField(choices=FILTER_CHOICES)

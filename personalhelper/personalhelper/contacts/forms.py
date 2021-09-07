from django.db.models.fields import BLANK_CHOICE_DASH
from django.forms.fields import NullBooleanField
from .models import Contact, Phone
from django.forms import ModelForm
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model = Contact

        fields = ['contact_name', 'contact_email', 'contact_birthday', 'contact_adress']

class PhoneForm(ModelForm):
    class Meta:
        model = Phone

        fields = ['phone']

class SearchForm(forms.Form):
    contact_name = forms.CharField(max_length=10)
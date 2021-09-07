from django import forms
from django.forms import ModelForm, widgets
from .models import Contact, Phone
from django.forms.fields import NullBooleanField
from django.db.models.fields import BLANK_CHOICE_DASH, CharField
from django.forms import ModelForm, HiddenInput
from .models import Contact


# class ContactCreateForm(ModelForm):
#     def clean_name(self):
#         data = self.cleaned_data['contact_name']
#         if len(data) < 50:
#             return data

#     class Meta:
#         model = Contact
#         fields = ['user', 'contact_name', 'contact_photo']
#         widgets = {'user': HiddenInput()}


# class ContactForm(ModelForm):
#     class Meta:
#         model = Contact

#         fields = ['contact_name', 'contact_phone',
#                   'contact_email', 'contact_birthday', 'contact_adress']


class ContactCreateForm(ModelForm):
    class Meta:
        model = Contact

        fields = ['user', 'contact_name', 'contact_email',
                  'contact_birthday', 'contact_adress']
        widgets = {'user': HiddenInput()}


class PhoneForm(ModelForm):
    class Meta:
        model = Phone

        fields = ['phone']


class SearchForm(forms.Form):
    contact_name = forms.CharField(max_length=10)

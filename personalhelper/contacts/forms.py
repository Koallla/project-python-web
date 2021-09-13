from django.db.models.fields import BLANK_CHOICE_DASH
from django.forms.fields import NullBooleanField
from .models import Contact, Phone
from django.forms import ModelForm, widgets
from django import forms


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        contact_birthday = forms.DateField(
            required=False, input_formats=['%Y-%m-%d', '%d.%m.%Y', '%d/%m/%Y'])
        fields = ['user', 'contact_name', 'contact_email',
                  'contact_birthday', 'contact_adress']
        widgets = {'user': forms.HiddenInput()}


class PhoneForm(ModelForm):
    class Meta:
        model = Phone

        fields = ['phone']


class SearchByName(forms.Form):
    contact_name = forms.CharField(max_length=10)


class SearchByDay(forms.Form):
    day_to_birthday = forms.IntegerField(max_value=360)

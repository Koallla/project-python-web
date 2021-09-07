from django.forms import ModelForm, HiddenInput
from .models import Contact


class ContactCreateForm(ModelForm):
    def clean_name(self):
        data = self.cleaned_data['contact_name']
        if len(data) < 50:
            return data

    class Meta:
        model = Contact
        fields = ['user', 'contact_name', 'contact_photo']
        widgets = {'user': HiddenInput()}

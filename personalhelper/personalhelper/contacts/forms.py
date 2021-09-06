from .models import Contact
from django.forms import ModelForm

class ContactForm(ModelForm):
    class Meta:
        model = Contact

        fields = ['contact_name', 'contact_phone', 'contact_email', 'contact_birthday', 'contact_adress']
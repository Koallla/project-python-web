from django.forms import ModelForm, fields
from .models import UserFile


class UserFileAdd(ModelForm):
    class Meta:
        model = UserFile
        fields = ['file', 'user', 'category']

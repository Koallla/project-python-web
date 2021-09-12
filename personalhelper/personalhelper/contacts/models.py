
from django.core import validators
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.db.models.deletion import CASCADE
from storages.backends.sftpstorage import SFTPStorage
from django.contrib.auth.models import User
SFS = SFTPStorage()


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    contact_name = models.CharField(max_length=50, null=False)
    contact_photo = models.FileField(storage=SFS, null=True, blank=True)
    contact_email = models.EmailField(null=False, blank=True)
    contact_adress = models.CharField(max_length=50, null=True, blank=True)
    contact_birthday = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return f'/contacts/show_contacts/{self.pk}'

    def __str__(self):
        return f'{self.contact_name}'


class Phone(models.Model):
    phone = models.CharField(max_length=10, validators=[validators.RegexValidator(
        regex='\d{10}$', message='Phone number must have 10 digits')])
    contact = models.ForeignKey(
        'Contact', on_delete=models.CASCADE)

    def __str__(self):
        return self.phone

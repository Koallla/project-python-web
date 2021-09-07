
from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from storages.backends.sftpstorage import SFTPStorage
from django.contrib.auth.models import User


SFS = SFTPStorage()


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    contact_name = models.CharField(max_length=50)
    contact_photo = models.FileField(
        upload_to='contacts/files/', storage=SFS, null=True, blank=True)
    contact_email = models.EmailField(null=False, blank=True)
    contact_adress = models.CharField(max_length=50, null=True, blank=True)
    contact_phone = models.CharField(
        max_length=10, null=False, default='0501111111')
    contact_birthday = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return f'/contacts/show_contacts/{self.pk}'

    def __str__(self):
        return f'{self.contact_name} | {self.contact_phone}'


class Phone(models.Model):
    value = models.CharField(max_length=10)
    contact = models.ForeignKey(
        'Contact', on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.value

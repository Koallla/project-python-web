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

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.contact_name


class Phone(models.Model):
    value = models.CharField(max_length=10)
    contact = models.ForeignKey(
        'Contact', on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.value

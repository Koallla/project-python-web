from django.db import models
from django.urls import reverse
from storages.backends.sftpstorage import SFTPStorage
SFS = SFTPStorage()


class Contact(models.Model):
    name = models.CharField(max_length=50)
    contact_photo = models.FileField(storage=SFS, null=True)

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.name


class Phone(models.Model):
    value = models.CharField(max_length=10)
    contact = models.ForeignKey(
        'Contact', on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.value

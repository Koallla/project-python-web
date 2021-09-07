from django import views
from django.db import models
from django.urls import reverse
from django.db.models.deletion import CASCADE
from storages.backends.sftpstorage import SFTPStorage
from django.contrib.auth.models import User
# Create your models here.

SFS = SFTPStorage()


class UserFile(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    file = models.FileField(upload_to='files/', storage=SFS)
    category = models.CharField(max_length=25)

    def get_absolute_url(self):
        return f'{self.file.name}'

    def __str__(self) -> str:
        return self.file.name

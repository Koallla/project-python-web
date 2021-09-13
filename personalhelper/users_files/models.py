from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.db.models.deletion import CASCADE
from storages.backends.sftpstorage import SFTPStorage
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
# Create your models here.

SFS = SFTPStorage()
LFS = FileSystemStorage()


def file_size(value):  # add this to some file where you can import it from
    limit = 5242880
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 5 MB.')


class UserFile(models.Model):
    CATEGORIES = [('videos', 'videos'), ('audios', 'audios'),
                  ('documents', 'documents'), ('fotos', 'fotos')]

    user = models.ForeignKey(User, on_delete=CASCADE)
    file = models.FileField(
        upload_to='files\\', storage=LFS, validators=[file_size])
    category = models.CharField(max_length=25, choices=CATEGORIES)

    def get_absolute_url(self):
        return f'{self.file.name}'

    def delete(self, using=None, keep_parents=False):
        self.file.storage.delete(self.file.name)
        super().delete()

    def __str__(self) -> str:
        filename = self.file.name.replace("files/", "")
        return f'{filename}'

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Tag(models.Model):
    title = models.CharField(max_length=20)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this Tag."""
        return reverse('notes:tag-detail', args=[str(self.id)])


class Note(models.Model):
    title = models.CharField(max_length=20)
    tags = models.ManyToManyField(Tag)
    value = models.TextField(max_length = 1000, default = 'LaLaLa')
    owner = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this Note."""
        return reverse('notes:note-detail', args=[str(self.id)])

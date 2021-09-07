from django.conf.urls import include, url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('files/<str:filename>', views.download_file),
    url(r'^create/', views.create_contact,
        name='contact-create'),
]

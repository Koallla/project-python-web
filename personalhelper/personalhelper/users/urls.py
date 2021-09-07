from django.conf.urls import include, url
from django.urls import path
from . import views


urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^register/', views.register, name='register'),
]

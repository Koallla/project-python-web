from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url(r'^create/', views.add_file,
        name='files-create'),
    url(r'^userfiles/$', views.UsersFilesView.as_view(), name='userfiles'),
    path('userfiles/files/<str:filename>', views.download_file),
]

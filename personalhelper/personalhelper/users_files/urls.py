from django.conf.urls import url, include
from django.urls import path
from . import views


urlpatterns = [
    url(r'^accounts/', include("django.contrib.auth.urls")),
    url(r'^create/', views.add_file,
        name='files-create'),
    # url(r'^userfiles/$', views.UsersFilesView.as_view(), name='userfiles'),
    path('userfiles/', views.files_all, name='userfiles'),
    path('userfiles/files/<str:filename>', views.download_file),
    path('delete/files/<int:id>', views.delete_file, name='delete-file'),
    path('category/<str:category_name>',
         views.files_by_categorie, name='category'),
]

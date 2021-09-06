from django.urls import path
from . import views


urlpatterns = [
    path('<str:filename>', views.download_file),
]

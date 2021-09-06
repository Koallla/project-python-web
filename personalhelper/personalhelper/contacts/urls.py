from django.urls import path
from . import views


urlpatterns = [
    path('<str:filepath>/', views.download_file),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.NoteListView.as_view(), name = 'notes'),
    path('notes/<int:pk>', views.NoteDetailView.as_view(), name='note-detail'),
    path('tags/', views.TagListView.as_view(), name = 'tags'),
    path('tags/<int:pk>', views.TagDetailView.as_view(), name='tag-detail'),
]
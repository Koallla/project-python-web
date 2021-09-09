from django.urls import path
from django.conf.urls import include, url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_notes/', views.NoteListView.as_view(), name='notes'),
    path('notes/<int:pk>', views.NoteDetailView.as_view(),
         name='note-detail'),
    path('tags/', views.TagListView.as_view(), name='tags'),
    path('tags/<int:pk>', views.TagDetailView.as_view(), name='tag-detail'),
]

urlpatterns += [
    path('notes/create/', views.NoteCreateView.as_view(), name='note-create'),
    path('notes/update/<int:pk>/', views.NoteUpdate.as_view(),
         name='note-update'),
    path('notes/delete/<int:pk>/', views.NoteDelete.as_view(),
         name='note-delete'),
]

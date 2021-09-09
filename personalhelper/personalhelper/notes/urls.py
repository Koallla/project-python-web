from django.urls import path
from django.conf.urls import include, url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('note/', views.NoteListView.as_view(), name='note'),
    path('note/<int:pk>/', views.NoteDetailView.as_view(), 
        name='note-detail'),
    path('tags/', views.TagListView.as_view(), name='tags'),
    path('tags/<int:pk>/', views.TagDetailView.as_view(), name='tag-detail'),
]

urlpatterns += [
    path('note/create/', views.NoteCreateView.as_view(), name='note-create'),
    path('note/update/<int:pk>/', views.NoteUpdate.as_view(),
         name='note-update'),
    path('note/<int:pk>/delete/', views.NoteDelete.as_view(),
         name='note-delete'),
    path('notes/create_tag/', views.TagCreate.as_view(), name = 'tag-create'),
]

from django.shortcuts import render
from django.views import generic
from .models import Tag, Note   


class NoteListView(generic.ListView):
    model = Note
    paginate_by = 10
    
class NoteDetailView(generic.DetailView):
    model = Note
    
class TagListView(generic.ListView):
    model = Tag
    paginate_by = 10
    
class TagDetailView(generic.DetailView):
    model = Tag

def index(request):
    """View function for home page for notes."""
    notes = Note.objects.all()
    notes_count = Note.objects.all().count()
    
    context = {'notes': notes, 'notes_count': notes_count}
    
    return render(request, 'index.html', context = context)
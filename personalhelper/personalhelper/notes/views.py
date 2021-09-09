from .forms import NoteCreateForm, NoteUpdateForm
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tag, Note
from django.views import generic
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


class NoteListView(LoginRequiredMixin, generic.ListView):
    model = Note
    paginate_by = 10

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

    def get_login_url(self) -> str:
        return settings.LOGIN_REDIRECT_URL


class NoteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Note

    def get_login_url(self) -> str:
        return settings.LOGIN_REDIRECT_URL


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    paginate_by = 10

    def get_login_url(self) -> str:
        return settings.LOGIN_REDIRECT_URL


class TagDetailView(LoginRequiredMixin, generic.DetailView):
    model = Tag

    def get_login_url(self) -> str:
        return settings.LOGIN_REDIRECT_URL


def index(request):
    """View function for home page for notes."""
    notes = Note.objects.all()
    notes_count = Note.objects.all().count()

    context = {'notes': notes, 'notes_count': notes_count}

    return render(request, 'index.html', context=context)


class NoteCreateView(LoginRequiredMixin, CreateView):
    form_class = NoteCreateForm
    template_name = 'notes/note_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_initial(self, *args, **kwargs):
        initial = super(NoteCreateView, self).get_initial(**kwargs)
        initial['title'] = 'My Title'
        return initial

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(NoteCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['owner'] = self.request.user
        return kwargs

    def get_login_url(self) -> str:
        return settings.LOGIN_REDIRECT_URL

class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteUpdateForm
    template_name = 'notes/note_form.html'

    def get_login_url(self) -> str:
        return settings.LOGIN_REDIRECT_URL

class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('notes')

    def get_login_url(self) -> str:
        return settings.LOGIN_REDIRECT_URL

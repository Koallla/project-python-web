from .forms import NoteCreateForm, NoteUpdateForm, AddTagForm
from django.conf import settings
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tag, Note
from django.views import generic
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


class NoteListView(LoginRequiredMixin, generic.ListView):
    model = Note
    paginate_by = 5

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


@login_required(login_url='login')
def index(request):
    # """View function for home page for notes."""
    # notes = Note.objects.all()
    # notes_count = Note.objects.filter(owner = request.user).count()

    # context = {'notes': notes, 'notes_count': notes_count}

    # return render(request, 'index.html', context=context)
    return NoteListView.as_view()(request)


@login_required(login_url='login')
def notes_by_tags(request, pk):
    tag = Tag.objects.get(pk=pk)
    notes_list = Note.objects.filter(owner=request.user.id).filter(tags=tag)

    paginator = Paginator(notes_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'notes/note_list.html', {'page_obj': page_obj, 'filtered': True, 'tag': tag})


class NoteCreateView(LoginRequiredMixin, CreateView):
    form_class = NoteCreateForm
    template_name = 'notes/note_form.html'

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.owner = self.request.user
    #     self.object.save()
    #     print(form.cleaned_data['tags'])
    #     # self.object.tags.set = form.cleaned_data['tags']
    #     # self.object.save()
    #     return HttpResponseRedirect(self.get_success_url())

    def get_initial(self, *args, **kwargs):
        initial = super(NoteCreateView, self).get_initial(**kwargs)
        initial['title'] = 'My Title'
        initial['owner'] = self.request.user
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
    success_url = reverse_lazy('notes:note')

    def get_login_url(self) -> str:
        return settings.LOGIN_REDIRECT_URL


class TagCreate(LoginRequiredMixin, CreateView):
    model = Tag
    form_class = AddTagForm
    template_name = 'notes/tag_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect(reverse_lazy('notes:note-create'))

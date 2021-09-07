from django.views.generic import DetailView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.template import loader
from django.shortcuts import redirect, render
from django.db.models import fields
from django import template
import mimetypes
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from storages.backends.sftpstorage import SFTPStorage


from .models import Contact
from .forms import ContactCreateForm


SFS = SFTPStorage()


# Create your views here.


def download_file(request):

    f_path = '/file'
    filename = 'file.ext'

    f = open(f_path, 'r')
    mime_type, _ = mimetypes.guess_type(f_path)
    response = HttpResponse(f, content_type=mime_type)
    response['Content-Disposition'] = f"attachment; filename={filename}"
    return response


def index(request):

    record_list = Contact.objects.all()
    template = loader.get_template('contacts/index.html')
    context = {
        'record_list': record_list
    }
   # return HttpResponse(template.render(context, request))
    return render(request, 'contacts/index.html')


def add_contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('/contacts/')
    else:
        form = ContactForm()
        return render(request, 'contacts/add_contact.html', {'form': form})


def show_all(request):
    contact_list = Contact.objects.order_by('contact_name')
    print(contact_list)
    template = loader.get_template('contacts/show_all.html')
    context = {
        'record_list': contact_list
    }
    return HttpResponse(template.render(context, request))


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contacts/detail_view.html'
    context_object_name = 'contact'


class ContactUpdateView(UpdateView):
    model = Contact
    template_name = 'contacts/update_contact.html'

    fields = ['contact_email', 'contact_birthday', 'contact_adress']


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = '/contacts/show_contacts'
    template_name = 'contacts/delete_view.html'

    # f_path = '/file'
    # filename = request['filename']
    # print(SFS.exists('files\\' + filename))
    if SFS.exists('contacts\\files\\' + filename):
        file = SFS._read('contacts\\files\\' + filename)
        mime_type, _ = mimetypes.guess_type(filename)
        print(mime_type)
        response = HttpResponse(file, content_type=mime_type)
        response['Content-Disposition'] = f"attachment; filename={filename}"
        return response


def index(request):
    return render(request, "contacts/index.html")


@login_required
def create_contact(request):
    if request.method == 'POST':
        form = ContactCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = ContactCreateForm(initial={'user': request.user})
    return render(request, 'contacts/create.html', {'form': form})


# class ContactCreate(CreateView):
#     model = Contact
#     fields = ['user', 'name', 'contact_photo']
#     initial = {'user': User}

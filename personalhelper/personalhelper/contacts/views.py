
from django import template
from django.db.models import fields
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Contact
from django.template import loader
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
import mimetypes


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
    




from django import template
from django.db.models import fields
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from .models import Contact, Phone
from django.template import loader
from .forms import ContactForm, SearchForm, PhoneForm
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
import re

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


def phone_chek(new_value):
    if not re.match('\d{10}$', new_value):
        raise ValueError('Phone number must have 10 digits')
    else:
        new_value = new_value


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
        form1 = PhoneForm(request.POST)
        if form.is_valid() and form1.is_valid():
            user = form.cleaned_data.get('user')
            name = form.cleaned_data.get('contact_name')
            email = form.cleaned_data.get('contact_email')
            adress = form.cleaned_data.get('contact_adress')
            birthday = form.cleaned_data.get('contact_birthday')

            phone = form1.cleaned_data.get('phone')
            phone_chek(phone)
            form = Contact(user=user, contact_name=name, contact_email=email,
                           contact_adress=adress, contact_birthday=birthday)
            form.save()
            form = Phone(phone=phone, contact=form)
            form.save()
            return redirect('/contacts/')
        else:
            return render(request, 'contacts/add_contact.html', {'form': form, 'form1': form1})
    else:
        form = ContactForm(initial={'user': request.user})
        form1 = PhoneForm()
        return render(request, 'contacts/add_contact.html', {'form': form, 'form1': form1})


def show_all(request):
    contact_list = Phone.objects.all()
    # print(contact_list)
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


def search(request):

    if request.method == 'POST':
        contact_list = Contact.objects.all()
        # contact = Contact.objects.get(headline__contains = )
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('contact_name')

            # print(name)
            try:
                contact = Contact.objects.get(contact_name__contains=name)

                template = loader.get_template('contacts/show_contact.html')
                context = {'record_list': contact}
                return HttpResponse(template.render(context, request))
            except:
                form = SearchForm()
                return render(request, 'contacts/search_contact.html', {'form': form})

            # return redirect('/contacts/')
    else:
        form = SearchForm()
        return render(request, 'contacts/search_contact.html', {'form': form})


def add_phone(request, id):
    form = PhoneForm()
    # print(id)

    try:
        person = Contact.objects.get(id=id)
        # print(1)

        if request.method == "POST":
            # print(2)
            forma = PhoneForm(request.POST)
            # print(6)
            print(forma)
            phone = forma.cleaned_data.get('phone')
            # print(3)
            phone1 = Phone(phone=phone, contact=person)
            phone1.save()
            return HttpResponseRedirect("/")
        else:
            # print(4)
            return render(request, 'contacts/add_phone.html', {'form': form})
    except:
        # print(5)

        form = PhoneForm()
        return render(request, 'contacts/add_phone.html', {'form': form})


class AddPhone(CreateView):
    model = Phone
    template_name = 'contacts/add_phone.html'
    fields = ['phone', 'contact']

from django import template
from django.conf.urls import url
from django.core.paginator import Paginator
from django.db.models import fields
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Contact, Phone
from django.template import loader
from .forms import ContactForm, SearchForm, PhoneForm
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
import re
from datetime import date, datetime

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


@login_required(login_url='login')
def index(request):
    contact_list = Contact.objects.filter(
        user_id=request.user.id)

    paginator = Paginator(contact_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'contacts/index.html', {'record_list': page_obj})


@login_required(login_url='login')
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


@login_required(login_url='login')
def show_all(request):
    contact_list = Contact.objects.filter(
        user_id=request.user.id)
    template = loader.get_template('contacts/show_all.html')
    context = {
        'record_list': contact_list
    }
    print(context)
    return render(request, 'contacts/show_all.html', {'record_list': contact_list})


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
    success_url = 'contacts/'
    template_name = 'contacts/delete_view.html'


@login_required(login_url='login')
def delete_record(request, pk):
    contact = Contact.objects.get(pk=pk)
    contact.delete()
    return index(request)


@login_required(login_url='login')
def delete_phone(request, pk):
    phone = Phone.objects.get(pk=pk)
    phone.delete()
    return index(request)


@login_required(login_url='login')
def search(request):

    if request.method == 'POST':
        contact_list = Contact.objects.filter(user=request.user.id)
        print(Contact._meta.fields)
        # print(contact_list)
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('contact_name')

            # print(name)
            try:
                contacts = contact_list.filter(contact_name__icontains=name)
                return render(request, 'contacts/index.html', {'record_list': contacts, 'mode': 'search'})
            except:
                error = 'No contacts with such name. Search is case sensitive'
                form = SearchForm()
                return render(request, 'contacts/index.html', {'form': form, 'error': error})
        else:
            error = 'No contats with sush name. Search is case sensitive'
            form = SearchForm()
            return render(request, 'contacts/search_contact.html', {'form': form, 'error': error})

    else:
        form = SearchForm()
        return render(request, 'contacts/search_contact.html', {'form': form})


@login_required(login_url='login')
def add_phone(request, id):
    form = PhoneForm()
    # print(id)
    person = Contact.objects.get(id=id)
    if request.method == "POST":
        forma = PhoneForm(request.POST)
        if forma.is_valid():
            phone = forma.cleaned_data.get('phone')
            phone1 = Phone(phone=phone, contact=person)
            phone1.save()
            return HttpResponseRedirect("/")
        else:
            error = 'Enter the valid phone. Phone number must have 10 digits'
            form = PhoneForm()
            return render(request, 'contacts/add_phone.html', {'form': forma, 'error': error, 'person': person})
    else:
        return render(request, 'contacts/add_phone.html', {'form': form, 'person': person})


def count_days(d_now, d_birth):
    if d_now > d_birth:
        d_birth = date(d_birth.year + 1, d_birth.month, d_birth.day)
    return (d_birth - d_now).days


@login_required
def days_to_birthday(request, id):

    birthday = Contact.objects.get(id=id)

    if birthday.contact_birthday != None:

        result = count_days(datetime.now().date(), date(year=datetime.now().year, month=int(
            birthday.contact_birthday.month), day=int(birthday.contact_birthday.day)))

        template = loader.get_template('contacts/bithday.html')
        context = {
            'record': birthday,
            'birthday': result
        }
        return HttpResponse(template.render(context, request))
    else:
        error = "This contact has not date of birthday"
        template = loader.get_template('contacts/bithday.html')
        context = {
            'error': error,
        }
        return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def filtered_by_day(request, days):
    contacts = request.GET.get('record_list')
    print(contacts)
    return render(request, 'contacts/index.html', {'record_list': contacts, 'mode': 'search'})

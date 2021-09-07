import mimetypes
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from storages.backends.sftpstorage import SFTPStorage


from .models import Contact
from .forms import ContactCreateForm


SFS = SFTPStorage()


# Create your views here.


def download_file(request, filename):

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

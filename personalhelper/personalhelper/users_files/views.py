import mimetypes
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views import generic
from storages.backends.sftpstorage import SFTPStorage
from django.core.files.storage import FileSystemStorage

from .models import UserFile
from .forms import UserFileAdd
# Create your views here.

SFS = SFTPStorage()
LFS = FileSystemStorage()


@login_required(login_url='login')
def add_file(request):
    if request.method == 'POST':
        form = UserFileAdd(request.POST, request.FILES)
        if form.is_valid():
            filename = request.FILES['file']
            print(mimetypes.guess_type(filename.name))
            if form.is_valid():
                form.save()
            return redirect('userfiles')
        else:
            return render(request, 'users_files/add.html', {'form': form})
    else:
        form = UserFileAdd(initial={'user': request.user})
    return render(request, 'users_files/add.html', {'form': form})


def download_file(request, filename):

    if LFS.exists('files/' + filename):
        file = LFS.open('files/' + filename)
        mime_type, _ = mimetypes.guess_type(filename)
        response = HttpResponse(file, content_type=mime_type)
        response['Content-Disposition'] = f"attachment; filename={filename}"
        return response


def delete_file(request, id):
    # if SFS.exists('files\\' + file):
    print(id)
    file = UserFile.objects.get(pk=id)
    file.delete()
    return redirect('userfiles')


def files_by_categorie(request, category_name):
    userfile_list = []
    userfile_list = UserFile.objects.filter(
        user_id=request.user.id).filter(category=category_name)
    return render(request, 'users_files/userfile_list.html', {'userfile_list': userfile_list, 'filtered': True, 'category': category_name})


def files_all(request):

    userfile_list = UserFile.objects.filter(
        user_id=request.user.id)

    paginator = Paginator(userfile_list, 10)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'users_files/userfile_list.html', {'userfile_list': page_obj, 'filtered': False})

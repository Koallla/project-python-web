import mimetypes
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views import generic
from storages.backends.sftpstorage import SFTPStorage

from .models import UserFile
from .forms import UserFileAdd
# Create your views here.

SFS = SFTPStorage()


@login_required(login_url='login')
def add_file(request):
    if request.method == 'POST':
        form = UserFileAdd(request.POST, request.FILES)
        if form.is_valid():
            filename = request.FILES['file']
            print(filename)
            print(mimetypes.guess_type(filename.name))
            if form.is_valid():
                form.save()
            return redirect('userfiles')
        else:
            return render(request, 'users_files/add.html', {'form': form})
    else:
        form = UserFileAdd(initial={'user': request.user})
    return render(request, 'users_files/add.html', {'form': form})


# class UsersFilesView(generic.ListView):

#     model = UserFile

#     def get_context_data(self, **kwargs):
#         paginate_by = 2
#         context = super(UsersFilesView, self).get_context_data(**kwargs)
#         userfile_list = UserFile.objects.filter(
#             user_id=self.request.user.id)
#         paginator = Paginator(userfile_list, paginate_by)
#         page = self.request.GET.get('page')
#         print(paginator.count)

#         try:
#             userfiles = paginator.page(page)
#         except PageNotAnInteger:
#             userfiles = paginator.page(1)
#         except EmptyPage:
#             userfiles = paginator.page(paginator.num_pages)
#         context['userfile_list'] = userfiles
#         return context


def download_file(request, filename):

    # f_path = '/file'
    # filename = request['filename']
    # print(SFS.exists('files\\' + filename))
    if SFS.exists('files\\' + filename):
        file = SFS._read('files\\' + filename)
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
    userfile_list = []
    userfile_list = UserFile.objects.filter(
        user_id=request.user.id)

    paginator = Paginator(userfile_list, 10)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'users_files/userfile_list.html', {'userfile_list': page_obj, 'filtered': False})

import mimetypes
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views import generic
from storages.backends.sftpstorage import SFTPStorage

from .models import UserFile
from .forms import UserFileAdd
# Create your views here.

SFS = SFTPStorage()


@login_required
def add_file(request):
    if request.method == 'POST':
        form = UserFileAdd(request.POST, request.FILES)
        filename = request.FILES['file']
        print(filename)
        print(mimetypes.guess_type(filename.name))
        if form.is_valid():
            form.save()
        return redirect('contacts:index')
    else:
        form = UserFileAdd(initial={'user': request.user})
    return render(request, 'users_files/add.html', {'form': form})


class UsersFilesView(generic.ListView):
    model = UserFile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userfile_list'] = UserFile.objects.filter(
            user_id=self.request.user.id)
        return context


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

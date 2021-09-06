import mimetypes
from django.core.files import storage
from django.shortcuts import render
from django.http import HttpResponse
from storages.backends.sftpstorage import SFTPStorage
SFS = SFTPStorage()

# Create your views here.


def download_file(request, filename):

    # f_path = '/file'
    # filename = request['filename']
    # print(SFS.exists('files\\' + filename))
    if SFS.exists('files\\' + filename):
        file = SFS._read('files\\' + filename)
        mime_type, _ = mimetypes.guess_type(filename)
        print(mime_type)
        response = HttpResponse(file, content_type=mime_type)
        response['Content-Disposition'] = f"attachment; filename={filename}"
        return response

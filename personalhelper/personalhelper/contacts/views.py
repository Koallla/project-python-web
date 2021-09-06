from django.shortcuts import render
from django.http import HttpResponse

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

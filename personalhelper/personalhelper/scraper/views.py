from django.shortcuts import render
from .models import Comand
from .soup import add_commands_to_db
from time import time


def index(request):
    time_start = time()
    add_commands_to_db()
    time_finish = time() - time_start
    print('---------------------- time finish:', time_finish)

    data = Comand.objects.all()
    return render(request, 'comands-table.html', {'comands': data})
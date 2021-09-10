from django.shortcuts import render
from .models import Comand
from .soup import add_commands_to_db


def index(request):
    add_commands_to_db()

    data = Comand.objects.all()
    return render(request, 'comands-table.html', {'comands': data})
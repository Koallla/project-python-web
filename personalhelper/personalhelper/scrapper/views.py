from django.shortcuts import redirect, render
from django.http import HttpResponse, request
import jsonlines


def index(request):
    with jsonlines.open('comands.jl') as reader:
        data = []
        for obj in reader:
            data.append(obj)

    return render(request, 'comands-table.html', {'comands': data} )

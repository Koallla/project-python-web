from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login

from users.forms import CustomUserCreationForm

# Create your views here.


def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html', {'form': CustomUserCreationForm})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("contacts:index"))
        else:
            return render(request, 'users/register.html', {'form': CustomUserCreationForm})

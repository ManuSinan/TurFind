from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.http import HttpResponse
from .forms import UserRegistrationForm, TurfOwnerRegistrationForm
from .models import LoginUser

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})

def register_turf_owner(request):
    if request.method == 'POST':
        form = TurfOwnerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = TurfOwnerRegistrationForm()
    return render(request, 'signup_turf_owner.html', {'form': form})

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('profile')
        else:
            return HttpResponse("Invalid credentials")
    else:
        return render(request, 'login.html')

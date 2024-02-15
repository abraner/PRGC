from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('/PRGCdatabase/home')
    else:
        form = CreateUserForm
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was creates for ' + user)
                return redirect('/PRGCdatabase/login')
        context = {'form': form}
        return render(request, 'PRGC/register.html', context)


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('/PRGCdatabase/home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/PRGCdatabase/home')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {}
        return render(request, 'PRGC/login.html', context)


def logoutuser(request):
    logout(request)
    return redirect('/PRGCdatabase/login')


@login_required(login_url='/PRGCdatabase/login')
def home(request):
    return render(request, 'PRGC/home.html')
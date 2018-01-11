from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.views.decorators import csrf
# Create your views here.

def login(request):
    args = {}
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        #print(auth.authenticate(username=username, password=password))
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            args['login_error'] = "Пользователь не найден"
            return render(request, 'login.html', args)
    else:
        return render(request, 'login.html', args)

def logout(request):
    auth.logout(request)
    return redirect("/")


def register(request):
    args = {}
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=request.POST["username"], password=request.POST["password1"])
            auth.login(request,newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render(request, "register0.html", args)


def registration(request):
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        is_val = form.is_valid()

        if is_val:
            data = form.cleaned_data
            if data['password'] != data['password2']:
                is_val = False
                form.add_error('password2', ['Пароли не совпадают'])
            if models.User.objects.filter(username=data['username']).exists():
                form.add_error('username',['Пользователь с данным логином уже существует'])
                is_val = False
            if models.User.objects.filter(email=data['email']).exists():
                form.add_error('email',['Пользователь с данной электронной почтой уже зарегестрирован'])
                is_val = False


        if is_val:
            customer = form.save(commit=False)
            customer.user = models.User.objects.create_user(data['username'], data['email'], data['password'])
            customer.save()
            return redirect('/')
    else:
        form = RegistrationForm()

    context['form'] = form
    return render(request, "register.html", context)
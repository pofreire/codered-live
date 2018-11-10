from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import RegistroUsuarioForm, LoginUsuarioForm
from django import forms


def Login(request):
    form = LoginUsuarioForm(request.POST or None)
    print(request.user.is_authenticated())
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/painel/')
    return render(request, 'login.html', {'form':form})

def Registrar(request):
    form = RegistroUsuarioForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        return redirect('/painel/')
    context = {
        'form':form
    }
    return render(request, 'registrar.html', context)

def Logout(request):
    logout(request)
    return redirect('/')

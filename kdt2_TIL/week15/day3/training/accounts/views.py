from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash


# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')


def re_index(_):
    return redirect('accounts:index')


def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    
    if request.method == 'GET':
        form = CustomAuthenticationForm()
    else:
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:index')


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    
    if request.method == 'GET':
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auth_login(request, user)
            return redirect('accounts:index')
        
    context = {
        'form': form,
    }
    return render(request, 'accounts/sign_up.html', context)


@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('accounts:index')


@login_required
def update(request):
    if request.method == 'GET':
        form = CustomUserChangeForm(instance=request.user)
    else:
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
        
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_pwd(request):
    if request.method == 'GET':
        form = PasswordChangeForm(request.user)
    else:
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:index')
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_pwd.html', context)
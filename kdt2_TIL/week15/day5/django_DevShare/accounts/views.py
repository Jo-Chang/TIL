from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm, CustomAuthenticationForm


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('posts:index')
    
    if request.method == "POST":
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')
    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form,
        'invisible': True,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('posts:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:index')
    
    alert = False
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if datetime.strptime(request.POST.get('birthday'), '%Y-%m-%d').date() > datetime.now().date():
            alert = True        
        if not alert and form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
        'alert': alert,
    }
    return render(request, 'accounts/signup.html', context)


@login_required   # anonymoususer에서 회원탈퇴 -> NotImplementedError오류
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('posts:index')


@login_required
def update(request):
    alert = False
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if request.user.birthday > datetime.now().date():
            alert = True        
        if not alert and form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
        'alert': alert,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request):
    if request.method == "POST":
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('posts:index')
    else:
        form = CustomPasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
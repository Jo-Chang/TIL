from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm, CustomAuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('posts:index')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')
        is_get = False
    else:
        form = CustomAuthenticationForm()
        is_get = True


    context = {
        'form': form,
        'is_get': is_get,
    }
    return render(request, 'accounts/login.html', context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:index')
        is_get = False
    else:
        form = CustomUserCreationForm()
        is_get = True
    
    context = {
        'form': form,
        'is_get': is_get,
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('posts:index')

def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def follows(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if request.user != person:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username)

@login_required
def update(request):
    User = get_user_model()
    user = User.objects.get(pk=request.user.pk)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        is_get = False
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', user.username)
    else:
        form = CustomUserChangeForm(instance=user)
        is_get = True

    context = {
        'form': form,
        'is_get': is_get,
    }
    return render(request, 'accounts/update.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        is_get = False
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:profile', user.username)
        
    else:
        form = CustomPasswordChangeForm(request.user)
        is_get = True
    context = {
        'form': form,
        'is_get': is_get
    }
    return render(request, 'accounts/change_password.html', context)
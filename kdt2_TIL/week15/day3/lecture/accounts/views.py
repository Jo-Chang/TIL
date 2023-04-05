from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    # 로그인 페이지 (GET)
    if request.method == 'GET':
        form = AuthenticationForm()
    # 로그인 실행 로직 (POST)
    else:
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'GET':
        # form = UserCreationForm()
        form = CustomUserCreationForm()
    else:
        # form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auth_login(request, user)    # 회원 가입 후 바로 로그인
            return redirect('articles:index')
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def delete(request):
    # print(request.user)
    # print(dir(request.user))
    request.user.delete()
    auth_logout(request)   # 세션 삭제  # 탈퇴 후 로그아웃 진행해야 함! 순서 중요!!
    return redirect('articles:index')


@login_required
def update(request):
    if request.method == 'GET':
        form = CustomUserChangeForm(instance=request.user)
    else:
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request):
    if request.method == 'GET':
        form = PasswordChangeForm(request.user)
    else:
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # update_session_auth_hash(request, request.user)   # 가능
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
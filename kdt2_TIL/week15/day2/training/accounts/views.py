from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')


def redirect_index(_):
    return redirect('accounts:index')


def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
    else:
        # form = AuthenticationForm(request, request.POST)
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:index')
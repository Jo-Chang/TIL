from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label = '사용자 름이',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='사용자 이름',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control w-50',
            }
        ),
    )
    password1 = forms.CharField(
        label='Password',
        widget = forms.PasswordInput(
            attrs={
                'class': 'form-control w-50',
            }
        ),
    )
    password2 = forms.CharField(
        label='Password Confirmation',
        widget = forms.PasswordInput(
            attrs={
                'class': 'form-control w-50',
            }
        ),
    )
    email = forms.CharField(
        label='이메일',
        widget = forms.EmailInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    firstname = forms.CharField(
        label='이름',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control w-25',
            }
        ),
    )
    lastname = forms.CharField(
        label='성',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control w-25',
            }
        ),
    )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # fields = ('username', 'password', 'email',)


class CustomUserChangeForm(UserChangeForm):
    email = forms.CharField(
        label='이메일',
        widget = forms.EmailInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    first_name = forms.CharField(
        label='이름',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control w-25',
            }
        ),
    )
    last_name = forms.CharField(
        label='성',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control w-25',
            }
        ),
    )
    
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
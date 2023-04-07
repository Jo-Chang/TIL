from datetime import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model, password_validation
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    # birthday = forms.DateField(label='test', widget=forms.SelectDateWidget())
    # email = forms.CharField(widget=forms.Textarea(attrs={'rows':20,}))
    password1 = forms.CharField(
        label="패스워드",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control custom-signup-form',
        }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="패스워드 확인",
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control custom-signup-form',
        }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'birthday')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control custom-signup-form',}),
            'first_name': forms.TextInput(attrs={'class': 'form-control custom-signup-form',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control custom-signup-form',}),
            'email': forms.TextInput(attrs={'class': 'form-control custom-signup-form',}),
            'birthday': forms.DateInput(attrs={'type': 'date', 'value': '2020-01-01', 'class': 'form-control custom-signup-form'}),
        }
        labels = {
            'username': '아이디',
            'email': '이메일',
            'birthday': '생일',
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'birthday')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control custom-update-form',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control custom-update-form',}),
            'email': forms.TextInput(attrs={'class': 'form-control custom-update-form',}),
            'birthday': forms.DateInput(attrs={'type': 'date', 'value': '2020-01-01', 'class': 'form-control custom-update-form'}),
        }
        labels = {
            'email': '이메일',
            'birthday': '생일',
        }


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='아이디',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control custom-login-field-form',
            }
        )
    )
    password = forms.CharField(
        label='패스워드',
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control custom-login-field-form',
            }
        )
    )
    class Meta:
        model = get_user_model()
        fields = '__all__'
        labels = {
            'username': 'asdf',
        }
        


class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('old_password', 'new_password1', 'new_password2')
        labels = {
            'old_password': '기존 비밀번호~~',
            'new_password1': 'new1',
            'new_password2': 'new2',
        }
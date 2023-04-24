from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm, UsernameField
from django import forms
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='닉네임',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'style': 'width:40%; min-width:300px;',
                'placeholder': '닉네임을 입력해주세요',
            }
        ),
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
    )
    
    email = forms.EmailField(
        label='이메일',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'style': 'width:40%; min-width:300px;',
                'placeholder': '이메일을 입력해주세요',
            }
        )
    )

    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'style': 'width:40%; min-width:300px;',                
                'placeholder': '비밀번호를 입력해주세요',
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'style': 'width:40%; min-width:300px;',                
                'placeholder': '비밀번호를 다시 입력해주세요',
            }
        )
    )
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', )

class CustomUserChangeForm(UserChangeForm):
    password = None

    username = forms.CharField(
        label='닉네임',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'style': 'width:40%; min-width:300px;',
                'placeholder': '닉네임을 입력해주세요',
            }
        )
    )
    
    email = forms.EmailField(
        label='이메일',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'style': 'width:40%; min-width:300px;',
                'placeholder': '이메일을 입력해주세요',
            }
        )
    )

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = (
            'username',
            'email',
        )

class CustomPasswordChangeForm(PasswordChangeForm):

    old_password = forms.CharField(
        strip=False,
        label='기존 비밀번호',
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "autofocus": True,
                'class': 'form-control',
                'style': 'width:40%; min-width:300px;',                
                'placeholder': '현재 비밀번호를 입력해주세요',
            }
        )
    )

    new_password1 = forms.CharField(
        label='새 비밀번호',
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                'class': 'form-control',
                'style': 'width:40%; min-width:300px;',                
                'placeholder': '새 비밀번호를 입력해주세요',
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )

    new_password2 = forms.CharField(
        label='새 비밀번호 재입력',
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                'class': 'form-control',
                'style': 'width:40%; min-width:300px;',                
                'placeholder': '새 비밀번호를 다시 입력해주세요',
            }
        )
    )

class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='닉네임',
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                'class': 'form-control',
                'style': 'width:40%; min-width:300px;',
                'placeholder': '닉네임을 입력해주세요',
            }
        )
    )

    password = forms.CharField(
        label='비밀번호',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                'class': 'form-control',
                'style': 'width:40%; min-width:300px;',                
                'placeholder': '비밀번호를 입력해주세요',
            }
        )
    )
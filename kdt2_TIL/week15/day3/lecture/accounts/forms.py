from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# from .models import User  # Django는 User에 대한 직접 참조를 권장하지 않음
# 아래와 같은 방법 권장
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # model = User    # 권장되지 않는 방법
        # Django 프로젝트의 내부적인 동작순서상으로 User 객체 코드는 존재하지만 
        # User 객체를 인식하지 못하는 경우가 존재함
        model = get_user_model()
        

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
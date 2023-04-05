# Week15-3

-   Django - Authentication System 2


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">

<br>[Parent Contents...](../../README.md/#til-today-i-learned)


## Contents
- [sample](#sample)

<br>


-----


## Introduction

- User 객체와 CUD
  + 회원 가입
  + 회원 탈퇴
  + 회원정보 수정
  + 비밀번호 변경


-----


## 회원 가입

- 회원 가입 - User 객체를 Create 하는 것

- `UserCreationForm()` : 회원 가입을 위한 built-in ModelForm

- 커스텀 유저 모델을 위해 재작성 해야 되는 forms
  + `UserCreationForm`
  + `UserChangeForm`

- **!!** `get_user_model()` : 현재 프로젝트에서 활성화된 사용자 모델(active user model)을 반환하는 함수
  + get_user_model()은 커스텀 User 모델을 자동으로 반환해줌
  + Django 프로젝트의 내부적인 동작순서상으로 User 객체 코드는 존재하지만 User 객체를 인식하지 못하는 경우가 존재함


-----


## 회원 탈퇴

- 회원 탈퇴 - User 객체를 Delete 하는 것

- `request.user.delete()`


-----


## 회원정보 수정

- 회원정보 수정 - User 객체를 Update 하는 것

- `UserChangeForm()` : 회원가입을 위한 built-in ModelForm
  > https://github.com/django/django/blob/stable/3.2.x/django/contrib/auth/forms.py#L135

- `CustomUserChangeForm()`에서 fields 재정의
  + `fields = ('email', 'first_name', 'last_name',)`
  > https://github.com/django/django/blob/stable/3.2.x/django/contrib/auth/forms.py#L135


-----


## 비밀번호 변경

- `PasswordChangeForm(user, ...)` - 비밀번호 변경을 위한 built-in Form

- 암호 변경 시 세션 무효화
  + `update_session_auth_hash(request, user)` - 암호 변경 시 세션 무효화 방지
  + 암호가 변경되어도 로그아웃 되지 않도록 새로운 password의 session data로 기존 session 업데이트


-----


## 로그인 사용자에 대한 접근 제한

- `is_authenticated` - 속성
  + 사용자가 인증 되었는지 여부를 알 수 있는 User model의 속성(attributes)
  + 모든 User에 대해서 항상 True, AnonymousUser에 대해서 항상 False
  + 권한과는 관련 없음, 활성화 상태나 유효한 세션과도 관계 없음

- `login_required` - 데코레이터
  + 인증된 사용자에 대해서면 view 함수를 실행시키는 데코레이터
  + 로그인 하지 않은 사용자의 경우 `/accounts/login` 주소로 redirect 시킴
  

-----


## Tips

- Decorator : 기존에 작성된 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능만을 추가 해주는 함수
```py
def hello(func):
  def wrapper():
    print('HIHI')
    func()
    print('HIHI')

  return wrapper

@hello
def bye():
  print('byebye')

bye()
```
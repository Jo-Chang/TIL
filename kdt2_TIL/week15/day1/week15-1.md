# Week15-1

-   Django - Form, Handling http requests


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">

<br>[Parent Contents...](../../README.md/#til-today-i-learned)


## Contents
- [Introduction](#introduction)
- [Django Form](#django-form)
- [Widgets](#widgets)
- [ModelForm](#modelForm)
- [Tips](#tips)


<br>


-----


## Introduction

- HTML form : 사용자로부터 form 요소를 통해 데이터를 주고받으나 유효성 검사를 진행해야 함

- 유효성 검사 : 수집한 데이터가 정확하고 유효한지 확인하는 과정


-----


## Django Form

- 사용자가 입력 데이터를 수집하고 처리 및 유효성 검증을 위한 도구
```py
# articles/forms.py

from django import forms 

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```
```py
# articles/views.py

from .forms import ArticleForm

def new(request):
  form = ArticleForm()
  context = {
    'form': form,
  }
  return render(request, 'articles/new.html', context)
```
```html
<!-- articles/new.html -->
<h1>NEW</h1>
<form action="{% url 'articles:create' %}" method="POST">
  {% csrf_token %}
  {{ form }}
  <input type="submit">
</form>
```


-----


## Widgets

- HTML 'input' element의 표현을 담당
```py
  ...
  content = forms.CharField(widget=forms.Textarea)
  ...
```


-----


## ModelForm

- Form : 사용자가 입력 데이터를 DB에 저장하지 않을 때 (ex.로그인)
- ModelForm : 사용자가 입력 데이터를 DB에 저장해야 할 때 (ex. 회원가입)
- Meta class : ModelForm의 정보를 작성하는 곳
  + Meta Data : 데이터에 대한 데이터
  + fields 및 exclude 속성 : 표시할 속성과 배제할 속성
```py
class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = ('title',)
```
```py
class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    exclude = ('title',)
```

- `is_valid()` : 유효성 검사를 실행하고, 데이터 유효한지 여부를 boolean으로 반환

- `save()` : DB 객체를 만들고 저장
  + 키워드 인자 instance 여부를 통해 <span>생성할지, 수정할지</span>를 경정


-----

## HTTP requests method

- new & create view 비교
  + 공통점 - 데이터 생성 로직을 구현하기 위함
  + 차이점 - new는 <span>GET method</span>만을, create는 <span>POST method</span> 요청만을 처리


-----


## Tips

- Widget 응용
```py
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control mb-2 me-3 title-width',
                'placeholder': '제목을 입력해주세요.',
                'maxlength': 10,
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content form-control mb-2 me-3 content-width',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={'required': '내용을 입력해주세요.'}
    )
    
    class Meta:
        model = Article
        fields = '__all__'
```

- flex 속성 가지면 크롬 개발자 도구에서 justify-content, align-content 테스트 가능
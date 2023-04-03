from django import forms
from .models import Todo
from datetime import datetime

class TodoForm(forms.ModelForm):
    title = forms.CharField(
        label = '할 일 제목',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '제목 입력',
                'maxlength': 15,
            }
        )
    )
    content = forms.CharField(
        label = '할 일 내용',
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control',
                'placeholder': '내용 입력',
                'rows': 10,
                'cols': 30,
            }
        ),
        error_messages={'required': '내용을 입력해주세요.'},
    )
    priority = forms.IntegerField(
        label = '우선 순위',
        max_value=20,
        min_value=0,
        widget = forms.NumberInput(
            attrs = {
                'class': 'form-control w-25',
                'placeholder': '우선 순위 입력',
                'value': 3,
            }
        )
    )
    deadline = forms.DateField(
        label = '마감 기한',
        widget = forms.DateInput(
            attrs = {
                'type': 'date',
                'class': 'form-control w-50',
                'value': datetime.now().strftime('%Y-%m-%d'),
            },
        )
    )
    
    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ('completed',)
from django import forms 
from .models import Article

# ver.1
"""
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
"""

# ver. 2
"""
class ArticleForm(forms.ModelForm):
    # Python Innerclass 아님!!
    # django ModelForm의 구조
    
    # ModelForm의 정보를 작성하는 곳
    class Meta:
        model = Article
        fields = '__all__'
"""        

# ver. 3
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
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'style': 'width:40%; min-width:300px;',
            }
        )
    )
    select1_content = forms.CharField(
        label='선택1',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'style': 'width:40%; min-width:300px;',
            }
        )
    )
    select2_content = forms.CharField(
        label='선택2',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'style': 'width:40%; min-width:300px;',
            }
        )
    )
    select1_image = forms.ImageField(
        label='선택1 이미지(선택사항)',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
                'style': 'width:40%; min-width:300px',
            }
        ),
        required=False,
    )
    select2_image = forms.ImageField(
        label='선택2 이미지(선택사항)',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
                'style': 'width:40%; min-width:300px',
            }
        ),
        required=False,
    )
    
    class Meta:
        model = Post
        fields = (
            'title', 
            'select1_content', 
            'select2_content', 
            'select1_image', 
            'select2_image',
            )
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='댓글 작성하기',
        widget=forms.Textarea(
            attrs={
                'rows':'3',
                'style': 'width:400px;',
                'class':'form-control',
            }
        )
    )
    class Meta:
        model = Comment
        fields = ('content', )
        # widgets = {
        #     'content': forms.Textarea(attrs={'rows':'3',}),
        # }

class CommentUpdateForm(forms.ModelForm):
    content = forms.CharField(
        label='댓글 수정하기',
        widget=forms.Textarea(
            attrs={
                'rows':'3',
                'style':'width:400px;',
                'class':'form-control',
            }
        )
    )
    class Meta:
        model = Comment
        fields = ('content', )
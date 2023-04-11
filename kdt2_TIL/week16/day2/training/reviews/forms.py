from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            
        }
        widgets = {
            
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )
        labels = {
            'content': '댓글',
        }
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'class':'form-control', 
                    'rows': '5',
                    'cols': '10',
                    }
                )
        }
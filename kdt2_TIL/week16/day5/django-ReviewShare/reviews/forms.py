from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user',)
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control',}),
            'content': forms.Textarea(attrs={'class':'form-control', 'rows':'5',}),
            'movie': forms.TextInput(attrs={'class':'form-control', }),
            'score': forms.NumberInput(attrs={'class':'form-control',}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        labels = {
            'content': '댓글',
        }
        widgets = {
            'content': forms.Textarea(attrs={'class':'form-control', 'rows':'2',})
        }
from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user',)
        # fields = '__all__'


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Comment
        fields = ('content',)

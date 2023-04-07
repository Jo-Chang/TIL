from django import forms
from .models import Post, Category


class PostForm(forms.ModelForm):
    my_choices = [
        (None,'카테고리를 선택하세요'),
        ('개발', '개발'), 
        ('CS', 'CS'),
        ('신기술', '신기술'),
    ]
    
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control custom-post-form',
                'placeholder': '제목 입력',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control custom-post-form',
                'placeholder': '내용 입력',
            }
        )
    )
    # category = forms.ChoiceField(
    #     error_messages={'required': '카테고리를 선택하세요'},
    #     # initial=(None,'카테고리'),
    #     widget=forms.Select(
    #         attrs={
    #             'class': 'form-select custom-post-category-form',
    #             }
    #         ),
    #     choices = my_choices
    #     # choices = [('개발', '개발'), ('CS', 'CS'), ('신기술', '신기술'), (None,'카테고리를 선택하세요')]
    # )
    q_set = Category.objects.all()
    CHOICES = ((item.pk, item.category) for item in q_set)
    category = forms.ModelChoiceField(
        # choices = CHOICES,
        queryset=q_set, 
        label='카테고리', 
        empty_label='카테고리를 선택하세요',
        widget=forms.Select,
        # to_field_name='category'
    )

    class Meta:
        model = Post
        # fields = '__all__'
        fields = (
            'title', 
            'content', 
            'category',
        )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
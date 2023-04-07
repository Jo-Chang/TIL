from operator import attrgetter

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Post, Category
from .forms import PostForm, CategoryForm


# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        # 'categories': [post[0] for post in Post.objects.distinct().values_list('category')],
        # 'categories': [i for i in Category.objects.all()],
        'categories': Category.objects.all(),
    }
    return render(request, 'posts/index.html', context)


@login_required
def detail(request, pk: int):
    post = Post.objects.filter(pk=pk)
    if not post:
        return redirect('posts:index')
    context = {
        'post': zip(
            ('제목', '내용', '카테고리', '작성일'), 
            attrgetter('title', 'content', 'category','created_at')(post[0])
        ),
        'pk': pk,
        # 'categories': [post[0] for post in Post.objects.distinct().values_list('category')],
        'categories': Category.objects.all(),
    }
    return render(request, 'posts/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
        
    context = {
        'form': form,
        'categories': Category.objects.all(),
    }
    return render(request, 'posts/create.html', context)


@login_required
def delete(_, pk: int):
    Post.objects.get(pk=pk).delete()
    return redirect('posts:index')


@login_required
def update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', pk)
    else:
        form = PostForm(instance=post)
        
    context = {
        'form': form,
        'pk': pk,
        # 'categories': [i for i in Category.objects.all()],
        'categories': Category.objects.all(),
    }
    return render(request, 'posts/update.html', context)


def category(request, pk):
    posts = Post.objects.filter(category=pk)
    context = {
        'posts': posts,
        'categories': Category.objects.all(),
    }
    return render(request, 'posts/index.html', context)


@user_passes_test(lambda u: u.is_superuser)
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = CategoryForm()
        
    context = {
        'form': form,
        'categories': Category.objects.all(),
    }        
    return render(request, 'posts/add_category.html', context)
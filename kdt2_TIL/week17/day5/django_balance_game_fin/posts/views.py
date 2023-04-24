from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm, CommentUpdateForm
from django.contrib.auth.decorators import login_required
import json

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def redirect_index(request):
    return redirect('posts:index')


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
        
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)


def detail(request, post_pk: int):
    post = Post.objects.get(pk=post_pk)
    comments = post.comment_set.all()
    comment_form = CommentForm()
    comment_updateform = CommentUpdateForm()
    context = {
        'post': post,
        'comment_form': comment_form,
        'comments': comments,
        'comment_updateform': comment_updateform,
    }
    return render(request, 'posts/detail.html', context)


@login_required
def answer(request, post_pk, answer):
    post = Post.objects.get(pk=post_pk)

    if request.user not in post.select1_user.all() and request.user not in post.select2_user.all():
        if answer == post.select1_content:
            post.select1_user.add(request.user)
        elif answer == post.select2_content:
            post.select2_user.add(request.user)
    
    return redirect('posts:detail', post_pk)


@login_required
def post_like(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if post.like_users.filter(pk=request.user.pk).exists():
        post.like_users.remove(request.user)
        is_liked = False
    else:
        post.like_users.add(request.user)
        is_liked = True
    
    context = {
        'is_liked': is_liked,
        'likes_count': post.like_users.count(),
    }
    return JsonResponse(context)


@login_required
def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()  
    return redirect('posts:detail', post.pk)


def comment_delete(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if request.user == comment.user:
        comment.delete()
    return redirect('posts:detail', post_pk)
    
    
@login_required
def comment_like(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if comment.like_users.filter(pk=request.user.pk).exists():
        comment.like_users.remove(request.user)
        is_liked = False
    else:
        comment.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
        'likes_count': comment.like_users.count(),
    }
    return JsonResponse(context)


def comment_update(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    
    if request.user == comment.user:
        if request.method == 'POST':
            r = list(request.POST.keys())
            js = json.loads(r[0])
            comment.content = js['content']
            comment.save()

    context = {
        'content': comment.content,
    }
    return JsonResponse(context)
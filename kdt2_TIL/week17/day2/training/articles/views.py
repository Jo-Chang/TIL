from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.core.paginator import Paginator


def index(request):
    articles = Article.objects.order_by('-pk')
    
    page = request.GET.get('page', '1')
    per_page = 5
    
    paginator = Paginator(articles, per_page)
    page_obj = paginator.get_page(page)
    
    context = {
        'articles': page_obj,
        'last_page': paginator.num_pages,
    }
    return render(request, 'articles/index.html', context)


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article_pk=article.pk)

    else:
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'articles/create.html', context)


@login_required
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.article = article
        comment.save()

    return redirect('articles:detail', article.pk)


@login_required
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()

    return redirect('articles:detail', article_pk)

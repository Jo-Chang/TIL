from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def mainpage(request):
    return redirect('articles:index')


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    print(article)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# new & create Ver.1
"""
def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)


def create(request):    
    form = ArticleForm(request.POST)
    
    if form.is_valid(): # 유효성 검사
        article = form.save()
        return redirect('articles:detail', article.pk)
    
    context = {
        'form': form,   # 유효성 검사를 실패한 form
    }
    return render(request, 'articles/new.html', context)
"""

# new & create Ver.2
def new_create(request):
    print('=========',request.method,'=========', sep='\n')
    # HTTP requests method가 POST라면
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    
    # POST가 아니라면 (GET이라면)
    else:
        form = ArticleForm()
        
    context = {
        'form': form,
    }
    return render(request, 'articles/new_create.html', context)
    

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# edit & update Ver.1
"""
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)    
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/edit.html', context)
"""

# edit & update Ver.1
def new_update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
        
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/new_update.html', context)
from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    print(article)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # new에서 보낸 사용자 데이터를 받음
    print('\n'*3 + '===========')
    print(request.GET)
    print('===========' + '\n'*3)
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    # 받은 데이터를 DB에 저장
    # sol1
    """
    article = Article()
    article.title = title
    article.content = content
    article.save()
    """
    
    # sol2
    # 저장 전 유효성 검사와 같은 추가 작업을 위해 2번 선택
    article = Article(title=title, content=content)
    article.save()
    
    # sol3
    """
    article = Article.objects.create(title=title, content=content)
    """
    
    # 결과 페이지 반환
    context = {
        'article': article,
    }
    return render(request, 'articles/create.html', context)
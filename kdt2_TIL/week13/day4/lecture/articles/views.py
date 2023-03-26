from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')


def dinner(request):
    context = {
        'foods': ['볶음밥', '보쌈', '서브웨이', '햄버거',],
    }
    return render(request, 'articles/dinner.html', context)


def search(request):
    return render(request, 'articles/search.html')


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    # request 분석
    print(request)
    print(type(request))
    print(dir(request)) # 내부 method 분석
    print(request.GET)
    print(request.GET.get('message'))
    
    # context = request.GET
    data = request.GET.get('message')
    context = {
        'message': data,
    }
    return render(request, 'articles/catch.html', context)


def detail(request, num):   # num 변수명 urls.py와 일치해야됨
    # num 변수로 DB에서 몇번 글을 조회하는지 검색할때 사용
    context = {
        'num': num,
    }
    return render(request, 'articles/detail.html', context)


def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/greeting.html', context)


def a(request):
    return render(request, '')
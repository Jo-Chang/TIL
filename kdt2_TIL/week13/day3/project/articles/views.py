from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': 'Creative',
    }
    return render(request, 'articles/index.html', context)


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
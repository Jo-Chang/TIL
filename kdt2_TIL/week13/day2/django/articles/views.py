from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'articles/index.html')

def berners_lee(request):
    return render(request, 'berners_lee.html')

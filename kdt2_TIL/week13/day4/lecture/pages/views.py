from django.shortcuts import render

# Create your views here.
def index(request):
    print('pages.index')
    return render(request, 'pages/index.html')
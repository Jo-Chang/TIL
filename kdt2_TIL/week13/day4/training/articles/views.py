from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    data = request.GET.get('data')
    context = {
        'data': data,        
    }
    return render(request, 'articles/catch.html', context)


def number_print(request, number):
    context = {
        'number': number,
    }
    return render(request, 'articles/number_print.html', context)


def calculate(request, number1, number2):
    n1, n2 = int(number1), int(number2)
    context = {
        'plus': n1 + n2,
        'minus': n1 - n2,
        'multiply': n1 * n2,
        'divisor': n1 // n2,
    }
    return render(request, 'articles/calculate.html', context)
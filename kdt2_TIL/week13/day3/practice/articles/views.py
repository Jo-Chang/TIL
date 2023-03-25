from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def today_dinner(request):
    foods = ['치킨', '삼겹살', '짜장면']
    food = random.choice(foods)
    print(food)
    context = {
        'food': food,
    }
    return render(request, 'articles/today_dinner.html', context)


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    query = request.GET.get('query')
    context = {
        'query': query,
    }
    return render(request, 'articles/catch.html', context)


def lotto_create(request):
    return render(request, 'articles/lotto_create.html')


def lotto(request):
    lotto_num = request.GET.get('number')
    # For case lotto_num is null
    if not lotto_num:
        lotto_num = 0
    # Convert to int
    lotto_num = int(lotto_num)
    print(lotto_num)
    # Generate lottery number list
    num_lst = [n for n in range(1, 46)]
    lottery_lst = []
    for _ in range(lotto_num):
        # Choose 6 lottery numbers 
        lst = random.sample(num_lst, k = 6)
        lottery_lst.append(lst)
        print(lst)
        
    context = {
        'num': lotto_num,
        'lottery_lst': lottery_lst,
    }
    return render(request, 'articles/lotto.html', context)
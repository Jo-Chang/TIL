"""
1. pk 필드가 1인 단일 데이터의 journalist 필드 조회
답 : Laney Mccullough
"""
Newspaper.objects.get(pk=1).journalist

"""
2. journalist 필드가 Laney Mccullough인 데이터 개수 조회
답 : 858
"""
len(Newspaper.objects.filter(journalist='Laney Mccullough'))

"""
3. pk 필드 기준 내림차순으로 정렬한 모든 데이터 조회
답 : <QuerySet [<Newspaper: Newspaper object (10000)>, <Newspaper: Newspaper object (9999)>, ...생략
"""
Newspaper.objects.order_by('-pk')

"""
4. created_at 필드 기준 내림차순으로 정렬한 모든 데이터 조회
답 : <QuerySet [<Newspaper: Newspaper object (4719)>, <Newspaper: Newspaper object (97)>, ...생략
"""
Newspaper.objects.order_by('-created_at')

"""
5. journalist 필드가 Britney를 포함하는 데이터 개수 조회
답 : 799
"""
len(Newspaper.objects.filter(journalist__contains='Britney'))

"""
6. journalist 필드가 ['Britney Mahoney', 'Arianna Walls', 'Carl Short']에 속하는 데이터 개수 조회
답 : 2469
"""
len(Newspaper.objects.filter(journalist__in=['Britney Mahoney', 'Arianna Walls', 'Carl Short']))

"""
7. created_at 필드가 2000-01-01 이후 데이터 개수 조회
답 : 4355
"""
len(Newspaper.objects.filter(created_at__gte='2000-01-01'))
Newspaper.objects.filter(created_at__gte='2000-01-01').count()

"""
8. 마지막 단일 데이터의 title, content, journalist 필드를 조회하고 아래와 같은 형식으로 출력
답
title : Teach father within million consumer baby its.
content : Then member effort want site. Radio represent yard bag fine. Congress movie ten along.
Hand receive agree science present main. Other member every.
journalist : Laney Mccullough
"""
# sol1
news = Newspaper.objects.last()
# news = Newspaper.objects.all().last()
# news = Newspaper.objects.order_by('pk').last()
# Newspaper.objects.order_by('-pk').first()
print(f'title : {news.title}')
print(f'content : {news.content}')
print(f'journalist : {news.journalist}')

# sol2
a = Newspaper.objects.order_by('-pk').values('title', 'content', 'journalist')
for k, v in a[0].items():
    print(f'{k} : {v}')


"""
기타 ORM 코드 작성 후 해당 코드와 결과 코드 리뷰 시간에 공유
"""
# __startswith
news = Newspaper.objects.filter(journalist__startswith='Laney')
people_lst = set()
for article in news:
    people_lst.add(article.journalist)
print(people_lst)

# __range
news = Newspaper.objects.filter(created_at__range=('2000-01-01', '2000-01-31'))
print(news)

# dates()
print(Newspaper.objects.filter(created_at__range=('2000-01-01', '2000-01-31')).dates('created_at', 'day'))

print(Newspaper.objects.dates('created_at', 'year'))
print(Newspaper.objects.dates('created_at', 'month'))
print(Newspaper.objects.dates('created_at', 'week'))
# All dates will be a Monday
print(Newspaper.objects.dates('created_at', 'day'))

# union()
# news1 = Newspaper.objects.get(pk=1)
# get일 경우 QuerySet이 아니므로 union 메서드 불가
news1 = Newspaper.objects.filter(pk=1)
news2 = Newspaper.objects.filter(pk=2)
news1.union(news2)

# get()
Newspaper.objects.filter(pk=1)
# <QuerySet [<Newspaper: Newspaper object (1)>]>
Newspaper.objects.filter(pk=1).get()
# <Newspaper: Newspaper object (1)>

# value
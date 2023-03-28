"""
1. 아래 할 일 생성
content : 실습 제출
priority : 5
completed : False
deadline : 오늘 날짜(년-월-일)
"""
import datetime
Todo.objects.create(content='실습 제출', priority=5, completed=False, deadline=datetime.today().strftime('%Y-%m-%d'))

"""
2. 아래 할 일 생성
content : 데일리 설문(오후) 제출
deadline : 오늘 날짜(년-월-일)
"""
from datetime import datetime
Todo.objects.create(content='데일리 설문(오후) 제출', deadline=datetime.today().strftime('%Y-%m-%d'))

"""
3. 임의의 할 일 5개 생성
"""
Todo.objects.create(content='밥 먹기', deadline=datetime.today().strftime('%Y-%m-%d'))
Todo.objects.create(content='과제 하기', deadline=datetime.today().strftime('%Y-%m-%d'))
Todo.objects.create(content='알고리즘 문제 풀이', deadline=datetime.today().strftime('%Y-%m-%d'))
Todo.objects.create(content='데일리 설문(오전) 제출', deadline=datetime.today().strftime('%Y-%m-%d'))
Todo.objects.create(content='데일리 설문(오후) 제출', deadline=datetime.today().strftime('%Y-%m-%d'))

"""
4. pk 기준 오름차순으로 정렬한 모든 데이터 조회
"""
Todo.objects.order_by('pk')

"""
5. priority 기준 내림차순으로 정렬한 모든 데이터 조회
"""
Todo.objects.order_by('-priority')

"""
6. pk가 1인 단일 데이터의 아래 필드 조회
(pk, content, priority, deadline, created_at)
"""
todo = Todo.objects.get(pk=1)
print(todo.pk, todo.content, todo.priority, todo.deadline, todo.created_at)
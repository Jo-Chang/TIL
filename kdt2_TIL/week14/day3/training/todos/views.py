from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)


def check_completed(request, todo_pk, todo_check):
    todo = Todo.objects.get(pk=todo_pk)
    todo.completed = todo_check
    todo.save()
    return redirect('todos:index')


def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)    
    priority = '★' * todo.priority
    context = {
        'todo': todo,
        'priority': priority,
    }
    return render(request, 'todos/detail.html', context)


def new(request):
    return render(request, 'todos/new.html')


def create(request):
    flag = True
    title = request.POST.get('title')
    content = request.POST.get('content')
    priority = request.POST.get('priority')
    deadline = request.POST.get('deadline')
    
    todo = Todo(title=title, content=content, priority=priority)
    if deadline:
        todo.deadline=deadline
    # 유효성 검사
    # if ...:
    #   flag = False
    if flag:
        todo.save()
    
    return redirect('todos:detail', todo.pk)


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    return redirect('todos:index')


def edit(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo,
    }
    return render(request, 'todos/edit.html', context)


def update(request, todo_pk):
    flag = True
    
    todo = Todo.objects.get(pk=todo_pk)
    title = request.POST.get('title')
    content = request.POST.get('content')
    priority = request.POST.get('priority')
    deadline = request.POST.get('deadline')
    
    todo.title = title
    todo.content = content
    todo.priority = priority
    if deadline:
        todo.deadline = deadline
    # 유효성 검사
    # if ...:
    #   flag = False
    if flag:
        todo.save()
        
    return redirect('todos:detail', todo.pk)
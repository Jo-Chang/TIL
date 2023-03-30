from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)


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
    if flag:
        todo.save()
    
    return redirect('todos:detail', todo.pk)


def delete(request, todo_pk):
    return redirect()


def edit(request, todo_pk):
    return render()


def update(request, todo_pk):
    return redirect()
from django.shortcuts import render
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
    context = {
        'todo': todo,
    }
    return render(request, 'todos/detail.html', context)


def new(request):
    return render(request, 'todos/new.html')


def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    priority = int(request.GET.get('priority'))
    deadline = request.GET.get('deadline')
    completed = True if request.GET.get('completed') else False
    
    todo = Todo(title=title, content=content, priority=priority, completed=completed) 
    if deadline:
        todo.deadline=deadline
    if Todo.objects.filter(title=title).count():
        todo.pk = Todo.objects.get(title=title).pk
        todo.title = None
        flag = False
        # return render(request, 'todos/create_fail.html')
    else:
        todo.save()
        flag = True
    
    context = {
        'flag': flag,
        'todo': todo,
    }
    return render(request, 'todos/create.html', context)
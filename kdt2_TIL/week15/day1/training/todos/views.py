from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)


def redirect_mainpage(_):
    return redirect('todos:index')
    

def check_completed(_, todo_pk, todo_check):
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


def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm()

    context = {
        'form': form,
    }
    return render(request, 'todos/create.html', context)


def update(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm(instance=todo)
    
    context = {
        'form': form,
        'todo': todo,
    }
    return render(request, 'todos/update.html', context)


def delete(_, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    return redirect('todos:index')
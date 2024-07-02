from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Todo_Data
from .forms import Todo_Form

def get_todo(request: HttpRequest) -> HttpResponse:
    todoList = Todo_Data.objects.all()
    return render(
        request=request, 
        template_name='todo.html', 
        context={
            'title': 'Todo Web App',
            'todoList': todoList,
        },
        content_type='text/html',
        status=200
    )

def add_todo(request: HttpRequest) -> HttpResponse:
    todoList = Todo_Data.objects.order_by('date')
    if request.method == 'POST':
        form = Todo_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    
    form = Todo_Form()
    return render(
        request=request, 
        template_name='add_todo.html', 
        context={
            'form': form,
        },
        content_type='text/html',
        status=200
    )


def update_todo(request: HttpRequest, id: int) -> HttpResponse:
    todo = get_object_or_404(Todo_Data, id=id)
    if request.method == 'POST':
        form = Todo_Form(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo')
        
    form = Todo_Form(instance=todo)
    return render(
        request=request, 
        template_name='update_todo.html', 
        context={
            'form': form,
            'todo': todo,
        },
        content_type='text/html', 
        status=200,
    )

def update_todo_done(request: HttpRequest, id:int) -> HttpResponse:
    todo = get_object_or_404(Todo_Data, id=id)
    todo.done = not todo.done
    todo.save()
    return redirect('todo')

def delete_todo(request: HttpRequest, id: int) -> HttpResponse:
    todo = get_object_or_404(Todo_Data, id=id)
    todo.delete()
    return redirect('todo')

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Todo_Data
from .forms import Todo_Form, User_Form


def get_todo(request: HttpRequest) -> HttpResponse:
    if request.user.is_anonymous:
        return redirect('login')
    todoData = Todo_Data.objects.filter(user=request.user)
    return render(
        request=request, 
        template_name='todo.html', 
        context={
            'request': request,
            'title': 'Todo Web App',
            'todoList': todoData,
        },
        content_type='text/html',
        status=200
    )

def add_todo(request: HttpRequest) -> HttpResponse:
    if request.user.is_anonymous:
        return redirect('login')
    if request.method == 'POST':
        form = Todo_Form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
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
    if request.user.is_anonymous:
        return redirect('login')
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
    if request.user.is_anonymous:
        return redirect('login')
    todo = get_object_or_404(Todo_Data, id=id)
    todo.done = not todo.done
    todo.save()
    return redirect('todo')

def delete_todo(request: HttpRequest, id: int) -> HttpResponse:
    if request.user.is_anonymous:
        return redirect('login')
    todo = get_object_or_404(Todo_Data, id=id)
    todo.delete()
    return redirect('todo')


def signup(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = User_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    
    form = User_Form()
    return render(
        request=request, 
        template_name='auth.html', 
        context={
            'title': 'Sign Up',
            'form': form,
        },
        content_type='text/html',
        status=200
    )

def login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = User_Form(request.POST)      
        username = form.data['username']
        password = form.data['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:    
            auth_login(request, user)
            print('Login Success')     
            return redirect('todo') 
    
    form = User_Form()
    return render(
        request=request, 
        template_name='auth.html', 
        context={                   
            'title': 'Login',
            'form': form,
        },
        content_type='text/html',
        status=200
    )

def logout(request: HttpRequest) -> HttpResponse:
    auth_logout(request)
    return redirect('login')
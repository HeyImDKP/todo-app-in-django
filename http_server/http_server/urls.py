"""
URL configuration for http_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.get_todo, name='todo'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('update_todo/<int:id>/', views.update_todo, name='update_todo'),
    path('update_todo_done/<int:id>/', views.update_todo_done, name='update_todo_done'),
    path('delete_todo/<int:id>/', views.delete_todo, name='delete_todo'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]

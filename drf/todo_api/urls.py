from django.urls import path
from .views import (
    TodoDataList,
    TodoDataDetail
)

urlpatterns = [
    path('todo/', TodoDataList.as_view(), name='todo_api'),
    path('todo/<int:pk>/', TodoDataDetail.as_view(), name='todo_api_detail'),
]
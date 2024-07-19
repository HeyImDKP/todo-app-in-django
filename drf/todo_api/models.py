from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class TodoData(models.Model):
    title = models.CharField(max_length=64)
    details = models.TextField(max_length=256, blank=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    done = models.BooleanField(default=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_list', null=True)

    ordering = ['-date', '-done']

    def __str__(self) -> str:
        return self.title
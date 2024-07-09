from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Todo_Data(models.Model):
    title = models.CharField(max_length=160)
    details = models.TextField()
    date = models.DateField(default=timezone.now)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_list', null=True, blank=True)

    class Meta:
        ordering = ['done', 'date']

    def __str__(self):
        return self.title

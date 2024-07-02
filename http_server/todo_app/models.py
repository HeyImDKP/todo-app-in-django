from django.db import models
from django.utils import timezone

# Create your models here.
class Todo_Data(models.Model):
    title = models.CharField(max_length=160)
    details = models.TextField()
    date = models.DateField(default=timezone.now)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

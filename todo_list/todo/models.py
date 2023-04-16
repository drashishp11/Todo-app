from django.db import models
from django.utils import timezone

# Create your models here.
class Tasks_todo(models.Model):
    task = models.CharField(max_length=120)
    task_description = models.TextField()
    deadline = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    objects = models.Manager()

    def _str_(self):
        return self.task


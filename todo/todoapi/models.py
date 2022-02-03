from operator import mod
from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=60)
    description = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    # alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name



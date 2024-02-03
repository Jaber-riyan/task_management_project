from django.db import models
import datetime
from category.models import CategoryModel

# Create your models here.
class TaskModel(models.Model):
    task_title = models.CharField(max_length=200)
    task_description = models.TextField(max_length=1000)
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(CategoryModel)
    
    def __str__(self):
        return self.task_title
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo_items(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank= True)
    td_id = models.AutoField(primary_key=True) 
    todo_title = models.CharField(max_length=100)
    todo_description = models.TextField()
    todo_isdone = models.BooleanField(default=False)
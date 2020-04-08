from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
   user_id = models.IntegerField()
   categorie = models.CharField(max_length=20)
   important_level = models.IntegerField()
   content = models.CharField(max_length=100)
   time = models.CharField(max_length=20)

from django.db import models

# Create your models here.
from django.db import models

# Create your models here.Here I can create a table in DB
class Project(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  technology = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)


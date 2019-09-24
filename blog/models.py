from django.db import models

# Create your models here.

class Blog(models.Model):
    blogger_name=models.CharField(max_length=10)
    massage = models.CharField(max_length=200)
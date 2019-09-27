from django.db import models


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    message = models.TextField()
    image = models.ImageField(upload_to='images/')

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class BlogModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    descriptions = models.TextField(blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f'Title: {self.title}'

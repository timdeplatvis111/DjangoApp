from django.db import models
from django.urls import reverse

# Create your models here.
# blogs/models.py

class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    text = models.TextField()

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return self.title
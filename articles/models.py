from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# capital for the first letter for the class/ model name is conventional
class Article(models.Model):
    """docstring for Article. Auto_now_add will automatically add the tiime and date"""
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    thumb = models.ImageField(default="default.png", blank=True)


    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100] + '...'

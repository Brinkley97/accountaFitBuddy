from .import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class CreateArticle(forms.ModelForm):
    """docstring for CreateArticle."""
    class Meta:
        model = models.Article
        fields = (
            'topic',
            'title',
            'body',
            'slug',
            'image',
            'video'
        )
        labels = {
            'image':('Upload Image'),
            'video':('Upload Video')
        }

class EditArticle(UserChangeForm):
    """docstring for EditArticle."""
    class Meta:
        model = models.Article
        fields = (
            'topic',
            'title',
            'body',
            'slug',
            'image',
            'video'
        )
        labels = {
            'image':('Upload Image'),
            'video':('Upload Video')
        }
        def save(self, commit=True):
            if commit:
                user.save()
            return user

class CreateComment(forms.ModelForm):
    """docstring for CreateComment."""
    class Meta:
        model = models.Comment
        fields = ['comment']

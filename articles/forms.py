from django import forms
from .import models
from django.contrib.auth.forms import UserChangeForm

class CreateArticle(forms.ModelForm):
    """docstring for CreateArticle."""
    class Meta:
        model = models.Article
        fields = ['title','body','slug','image','video']
        labels = {
            'image':('Upload Image'),
            'video':('Upload Video')
        }
class EditArticle(UserChangeForm):
    """docstring for EditArticle."""
    class Meta:
        model = models.Article
        fields = ['title','body','slug','image','video']
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

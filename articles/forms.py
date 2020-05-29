from django import forms
from .import models

class CreateArticle(forms.ModelForm):
    """docstring for CreateArticle."""
    class Meta:
        model = models.Article
        fields = ['title','body','slug','thumb']

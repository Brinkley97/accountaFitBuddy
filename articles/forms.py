from django import forms
from .import models

class CreateArticle(forms.ModelForm):
    """docstring for CreateArticle."""
    class Meta:
        model = models.Article
        fields = ['title','body','slug','image','video']


        labels = {
            'image':('Upload Image'),
            'video':('Upload Video')
        }

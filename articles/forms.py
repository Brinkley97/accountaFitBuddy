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
class CreateComment(forms.ModelForm):
    """docstring for CreateComment."""
    class Meta:
        model = models.Comment
        fields = ['comment']

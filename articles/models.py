from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# capital for the first letter for the class/ model name is conventional
class Article(models.Model):
    """docstring for Article. Auto_now_add will automatically add the tiime and date"""
    title = models.CharField(max_length=100, unique=True, blank=True)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", blank=True)
    video = models.FileField(default="default.mp4", blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100] + '...'

class Comment(models.Model):
    """
    docstring for Comment.
    many-to-one relationship with the Post model
    every comment will be made on a post
    each post will have multiple comments

    related_name attribute allows to name the attribute in use
    related_name can retrieve the post of a comment object using comment.post
    retrieve all comments of a post using post.comments.all()

    """
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    comment = models.TextField(default=None)
    date = models.DateTimeField(default=timezone.now)
    approvedComment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.author)

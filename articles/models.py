from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class Article(models.Model):
    TOPIC_CHOICES = (('Mental', 'Mental'), ('Food', 'Food'), ('Sleep', 'Sleep'), ('Exercise', 'Exercise'))

    topic = MultiSelectField(
        choices=TOPIC_CHOICES,
        default=None,
        min_choices=1,
        error_messages={
            "topic":"Select at least one topic your post entails."
        }
    )
    title = models.CharField(max_length=100, unique=True, blank=True)
    slug = models.SlugField(unique=True)
    body = models.TextField(blank=True)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", blank=True)
    video = models.FileField(default="default.mp4", blank=True)
    #related_name is like a ForeignKey; the way to associate like to the User
    likes = models.ManyToManyField(User, related_name='blogPosts')

    def totalLikes(self):
        return self.likes.count()
        
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

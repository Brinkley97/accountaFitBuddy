from django.db import models
from django import forms
from django.contrib.auth.models import User
from accounts.forms import MyRegistrationForm
from django.db.models import IntegerField, Model


class Health(models.Model):
    """docstring for HealthForm."""

    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('Prefer Not to State', 'Prefer Not to State'))
    AGE_CHOICES = [tuple([a,a]) for a in range(13,76)]
    HEIGHT_CHOICES = [tuple([c,c]) for c in range(0,101)]
    WEIGHT_CHOICES = [tuple([b,b]) for b in range(0,1001)]
    FITNESS_LEVEL = (('Beginner','Beginner'), ('Between Beginner and Intermediate','Between Beginner and Intermediate'), ('Intermediate','Intermediate'), ('Between Intermediate and Advanced','Between Intermediate and Advanced'), ('Advanced','Advanced'))
    GOAL_CHOICES = (('Lose Weight', 'Lose Weight'), ('Maintain', 'Maintain'), ('Bulk', 'Bulk'))

    author = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES)
    age = models.IntegerField(choices=AGE_CHOICES, blank=True)
    height = models.IntegerField(choices=HEIGHT_CHOICES, blank=True)
    weight = models.IntegerField(choices=WEIGHT_CHOICES, blank=True)
    fit = models.CharField(max_length=200, choices=FITNESS_LEVEL, blank=True)
    goal = models.CharField(max_length=200, choices=GOAL_CHOICES, blank=True)

    def __str__(self):
        return self.goal

class General(models.Model):
    """docstring for GereralForm."""

    GROUP_SIZE = [tuple([x,x]) for x in range(2,7)]
    OFTEN_CHOICES = (('1-2', '1-2'), ('3-4', '3-4'), ('5+', '5+'))

    author = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    thumbnail = models.ImageField(default="default.png", blank=True)
    location = models.CharField(max_length=100, blank=True)
    group = models.IntegerField(choices=GROUP_SIZE, blank=True)
    often = models.CharField(max_length=100, choices=OFTEN_CHOICES, blank=True)

    def __str__(self):
        return self.location

class Friend(models.Model):
    users = models.ManyToManyField(User)
    # look more into related_name
    # logined in user
    # null bc we don't have to have something or someone
    current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.SET_NULL)

# look more into the classmethod
    @classmethod
    def make_friend(cls, current_user, new_friend):
        # return an instance of friend
        friend, created = cls.objects.get_or_create(
            # check to see if the current object has that user as a friend
            current_user=current_user
        )

        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        # return an instance of friend
        friend, created = cls.objects.get_or_create(
            # check to see if the current object has that user as a friend
            current_user=current_user
        )
        friend.users.remove(new_friend)

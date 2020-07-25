from django.db import models
from django import forms
from django.contrib.auth.models import User
from accounts.forms import MyRegistrationForm
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator



class Health(models.Model):
    """docstring for HealthForm."""

    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('Prefer Not to State', 'Prefer Not to State'))
    FITNESS_LEVEL = (('Beginner','Beginner'), ('Between Beginner and Intermediate','Between Beginner and Intermediate'), ('Intermediate','Intermediate'), ('Between Intermediate and Advanced','Between Intermediate and Advanced'), ('Advanced','Advanced'))
    GOAL_CHOICES = (('Lose Weight', 'Lose Weight'), ('Maintain', 'Maintain'), ('Bulk', 'Bulk'), ('Other', 'Other'))

    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    thumbnail = models.ImageField(default="default.png", blank=True)
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES, blank=True)
    age = models.IntegerField(
        validators=[MinValueValidator(17), MaxValueValidator(80)],
        error_messages={
            "age":"The age requirement is between 17 and 80 years old."
        }
    )
    weight = models.IntegerField(
        validators=[MinValueValidator(50), MaxValueValidator(500)],
        error_messages={
            "weight":"The weight requirement is between 50lbs and 500lbs."
        },
        blank=True
    )
    fit = models.CharField(max_length=200, choices=FITNESS_LEVEL, blank=True)
    goal = models.CharField(max_length=200, choices=GOAL_CHOICES, blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.goal

class General(models.Model):
    """docstring for GereralForm."""

    OFTEN_CHOICES = (('1-2', '1-2'), ('3-4', '3-4'), ('5+', '5+'))

    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    group = models.IntegerField(
        validators=[MinValueValidator(2), MaxValueValidator(20)],
        error_messages={
            "group":"The group requirement is between 2 and 20."
        },
        blank=True
    )
    often = models.CharField(max_length=100, choices=OFTEN_CHOICES, blank=True)
    ig = models.CharField(max_length=100, blank=True)
    fb = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    snap = models.CharField(max_length=100, blank=True)
    whatsapp = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.often

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

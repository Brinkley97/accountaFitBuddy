from .import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import ugettext_lazy as _

class InsertHealth(forms.ModelForm):
    class Meta:
        model = models.Health
        fields = (
            'gender',
            'mental',
            'food',
            'sleep',
            'exercise',
            'age',
        )
        labels = {
            'food':_('Food & Nutrition'),
        }

class EditHealthForm(UserChangeForm):
    class Meta:
        model = models.Health
        fields = (
            'gender',
            'mental',
            'food',
            'sleep',
            'exercise',
            'age',
        )
        labels = {
            'food':_('Food & Nutrition'),
        }
        def save(self, commit=True):
            if commit:
                user.save()
            return user

class InsertGeneral(forms.ModelForm):
    class Meta:
        model = models.General
        fields = (
            'thumbnail',
            'location',
            'bio',
            'ig',
            'fb',
            'twitter',
            'snap',
            'whatsapp',
        )
        labels = {
            'thumbnail':_('Profile Picture'),
            'location':_('Enter your city and state'),
            'bio':_('Short description of your health journey'),
            'ig':_('Instagram'),
            'fb':_('Facebook'),
            'twitter':_('Twitter'),
            'snap':_('Snapchat'),
            'whatsapp':_('WhatsApp'),
        }

class EditGeneralForm(forms.ModelForm):
    class Meta:
        model = models.General
        fields = (
            'thumbnail',
            'location',
            'bio',
            'ig',
            'fb',
            'twitter',
            'snap',
            'whatsapp',
        )
        labels = {
            'thumbnail':_('Profile Picture'),
            'location':_('Enter your city and state'),
            'bio':_('Short description of your health journey'),
            'ig':_('Instagram'),
            'fb':_('Facebook'),
            'twitter':_('Twitter'),
            'snap':_('Snapchat'),
            'whatsapp':_('WhatsApp'),
        }
        def save(self, commit=True):
            if commit:
                user.save()
            return user

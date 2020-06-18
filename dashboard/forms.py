from django import forms
from .import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class InsertHealth(forms.ModelForm):
    """docstring for InsertHealth."""

    class Meta:
        model = models.Health

        fields = (
            'thumbnail',
            'gender',
            'age',
            'weight',
            'fit',
            'goal',
            'location',
            )

        labels = {
            'location':_('What is your desired location?'),

            'weight':_('Weight in lbs'),
        }

class InsertGeneral(forms.ModelForm):
    """docstring for InsertGeneral."""

    class Meta:
        model = models.General

        fields = ['group','often','ig','fb','twitter','snap','whatsapp']

        labels = {

        'group':_('Select up to how many you would like including yourself'),

        'often':_('How often do you go per week?'),

        'ig':_('Instagram'),
        'fb':_('Facebook'),
        'twitter':_('Twitter'),
        'snap':_('Snapchat'),
        'whatsapp':_('WhatsApp'),
        }

class EditProfileForm(UserChangeForm):
    class Meta:
        model = models.Health
        fields = (
            'thumbnail',
            'gender',
            'age',
            'weight',
            'fit',
            'goal',
            'location'

            )

        labels = {
            'location':_('What is your desired location?'),

            'weight':_('Weight in lbs'),
        }

        def save(self, commit=True):
            if commit:
                user.save()

            return user

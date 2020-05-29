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
            'gender',
            'age',
            'height',
            'weight',
            'fit',
            'goal'
            )

        labels = {
            'height':_('Add your height in inches.'),

            'weight':_('Weight in lbs'),
        }

class InsertGeneral(forms.ModelForm):
    """docstring for InsertGeneral."""

    class Meta:
        model = models.General

        fields = ['location','group','often', 'thumbnail']

        labels = {
        'location':_('What is your desired location?'),

        'group':_('Select up to how many you would like including yourself'),

        'often':_('How often do you go per week?')
        }

class EditProfileForm(UserChangeForm):
    class Meta:
        model = models.Health
        fields = (
            'gender',
            'age',
            'height',
            'weight',
            'fit',
            'goal',
            'password'

            )

        labels = {
            'height':_('Add your height in inches.'),

            'weight':_('Weight in lbs'),
        }

        def save(self, commit=True):
            if commit:
                user.save()

            return user

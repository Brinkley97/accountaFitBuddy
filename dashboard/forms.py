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

class EditHealthForm(UserChangeForm):
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

class EditGeneralForm(forms.ModelForm):
    """docstring for EditGeneralForm."""

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

        def save(self, commit=True):
            if commit:
                user.save()
            return user


            # https://stackoverflow.com/questions/12848605/django-modelform-what-is-savecommit-false-used-for
            # https://www.google.com/search?sxsrf=ALeKk03BT3ijP7yWNAi4NkOGWF42wKF24Q%3A1592520882021&ei=svDrXplt0Of9BqLZq8gH&q=++++++++user+%3D+super%28%29.save%28commit%3DFalse%29&oq=++++++++user+%3D+super%28%29.save%28commit%3DFalse%29&gs_lcp=CgZwc3ktYWIQAzoECAAQR1CbuAtYm7gLYIy6C2gAcAJ4AIABkgGIAZIBkgEDMC4xmAEAoAECoAEBqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwiZjuHLuozqAhXQc98KHaLsCnkQ4dUDCAw&uact=5
            # https://docs.djangoproject.com/en/3.0/topics/auth/customizing/
            # https://github.com/Brinkley97/accountaFitBuddy/commit/75f0d6a353b5be9f767fd3c38a11a547195f6cc5

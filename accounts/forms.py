from django import forms
from .import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
    """docstring for RegistrationForm."""
    email = forms.EmailField(required=True)

    class Meta:
        """docstring for Meta ."""
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
            )

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)

        if commit:
            user.save()

        return user

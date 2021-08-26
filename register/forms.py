from django import forms
from user.models import User
from django.db import models

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields  = [
            'email',
            'name',
            'password',
            'details',
        ]
class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    name = forms.CharField(label="Name",max_length=256)
    password = forms.CharField(label="Password",max_length=50)


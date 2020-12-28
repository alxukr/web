from django import forms
from django.db import models
from django.contrib.auth.models import User


class AnswerForm(forms.Form):
    text = forms.CharField(widget = forms.Textarea)
    question = forms.IntegerField()

class AskForm(forms.Form):
    title = forms.CharField(max_length = 50)
    text = forms.CharField(widget = forms.Textarea)

class SignupForm(forms.ModelForm):
    email = forms.CharField(label = 'email', required = True)
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username']

class LoginForm(forms.Form):
    username = forms.CharField(label = 'username', required = True)
    password = forms.CharField(label = 'password', widget=forms.PasswordInput)



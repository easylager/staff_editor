from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ['username', 'full_name', 'email', 'password1', 'password2', 'department', 'position']

class DepartmentForm(forms.Form):
    class Meta:
        model = Department
        fields = ['department']

class PositionForm(forms.Form):
    class Meta:
        model = Position
        fields = ['position']
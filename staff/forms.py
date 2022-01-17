from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ['username', 'full_name', 'email', 'password1', 'password2', 'department', 'position']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['department', 'position']
        widgets = {
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'})}


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['title', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})}

        labels = {
            'title': "Title",
            "slug": "Slug - Optional field"
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('It can not be created')
        return new_slug


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})}
        labels = {
            'title': "Title",
            "slug": "Slug - Optional field"
        }


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('It can not be created')
        return new_slug
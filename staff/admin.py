from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegistrationForm
from .models import *

class EmployeeUserAdmin(UserAdmin):
    add_form = UserRegistrationForm
    model = Employee
    list_display = ['full_name', 'department', 'position', 'password']

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Position)



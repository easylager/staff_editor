from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .utils import *
from django.views.generic import View
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'staff/base.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'staff/base.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return render(request, 'staff/authorization.html', {'form': form})


def register(request):
    if request.method == 'POST':

        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login_url')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'staff/registration.html', context={'form': user_form})





class EmployeesList(LoginRequiredMixin, ObjectListMixin, View):
    model = Employee
    template = 'staff/list/employees_list.html'
    raise_exception = True


class EmployeeDetail(LoginRequiredMixin, ObjectDetailMixin, View):
    model = Employee
    template = 'staff/detail/employee.html'


class EmployeeUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Employee
    model_form = EmployeeForm
    template = 'staff/update/employee.html'
    raise_exception = True


class DepartmentsList(LoginRequiredMixin, ObjectListMixin, View):
    model = Department
    template = 'staff/list/departments_list.html'
    raise_exception = True


class DepartmentCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model = Department
    model_form = DepartmentForm
    template = 'staff/create/department.html'
    redirect_template = 'staff/list/departments_list.html'
    raise_exception = True


class DepartmentUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Department
    model_form = DepartmentForm
    template = 'staff/update/department.html'
    raise_exception = True


class DepartmentDelete(LoginRequiredMixin, ObjectsDeleteMixin, View):
    model = Department
    template = 'staff/delete/department.html'
    link = 'departments_list_url'
    raise_exception = True


class DepartmentDetail(LoginRequiredMixin, ObjectDetailMixin, View):
    model = Department
    template = 'staff/detail/department.html'
    raise_exception = True


class PositionsList(LoginRequiredMixin, ObjectListMixin, View):
    model = Position
    template = 'staff/list/positions_list.html'
    raise_exception = True


class PositionCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model = Position
    model_form = PositionForm
    template = 'staff/create/position.html'
    redirect_template = 'staff/list/positions_list.html'
    raise_exception = True


class PositionUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Position
    model_form = PositionForm
    template = 'staff/update/position.html'
    raise_exception = True


class PositionDelete(LoginRequiredMixin, ObjectsDeleteMixin, View):
    model = Position
    template = 'staff/delete/position.html'
    link = 'positions_list_url'


class PositionDetail(LoginRequiredMixin, ObjectDetailMixin, View):
    model = Position
    template = 'staff/detail/position.html'
    raise_exception = True


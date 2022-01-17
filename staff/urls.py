from django.urls import path
from .views import *
from django.urls import include

urlpatterns = [
    path('', home, name='home_url'),
    path('login/', user_login, name='login_url'),
    path('register/', register, name='register_url'),
    path('departments_list/', DepartmentsList.as_view(), name='departments_list_url'),
    path('positions_list/', PositionsList.as_view(), name='positions_list_url'),
    path('employees_list/', EmployeesList.as_view(), name='employees_list_url'),
    path('employee/<str:slug>/detail', EmployeeDetail.as_view(), name='employee_detail_url'),
    path('employee/<str:slug>/update', EmployeeUpdate.as_view(), name='employee_update_url'),
    path('department/create', DepartmentCreate.as_view(), name='department_create_url'),
    path('position/create', PositionCreate.as_view(), name='position_create_url'),
    path('department/<str:slug>/update', DepartmentUpdate.as_view(), name='department_update_url'),
    path('position/<str:slug>/update', PositionUpdate.as_view(), name='position_update_url'),
    path('department/<str:slug>/delete', DepartmentDelete.as_view(), name='department_delete_url'),
    path('position/<str:slug>/delete', PositionDelete.as_view(), name='position_delete_url'),
    path('position/<str:slug>/detail', PositionDetail.as_view(), name='position_detail_url'),
    path('department/<str:slug>/detail', DepartmentDetail.as_view(), name='department_detail_url')

]
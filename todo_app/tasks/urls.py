from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('tasks/', views.view_tasks),
    path('tasks/add/', views.add_task),
    path('tasks/<int:task_id>/edit/', views.edit_task),
    path('tasks/<int:task_id>/delete/', views.delete_task),
    path('tasks/<int:task_id>/status/', views.update_task_status),
    path('tasks/employee/', views.view_employee_tasks),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('employees/<int:employee_id>/delete/', views.delete_employee, name='delete_employee'),
    path('employees/<int:employee_id>/edit/', views.edit_employee, name='edit_employee'),
    path('employees/', views.view_employees, name='view_employees'),
]

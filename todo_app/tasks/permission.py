from rest_framework.permissions import BasePermission

class IsEmployer(BasePermission):
    """
    Custom permission to only allow employers to add/edit/delete tasks and manage employees.
    """
    def has_permission(self, request, view):
        # Check if the logged-in user is an employer
        return request.user.is_authenticated and request.user.role == 'employer'


class IsEmployee(BasePermission):
    """
    Custom permission to only allow employees to view and update their tasks.
    """
    def has_permission(self, request, view):
        # Check if the logged-in user is an employee
        return request.user.is_authenticated and request.user.role == 'employee'

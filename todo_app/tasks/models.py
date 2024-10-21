from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import CustomUserManager
from django.conf import settings

class UserProfile(AbstractUser):
    username = models.CharField(max_length=10, null=True, blank=True, default=None)
    phone_number = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=10, choices=[('employer', 'Employer'), ('employee', 'Employee')], default='employee')
    employer = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='employees')
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number


class Task(models.Model):
    STATUS_CHOICES = [
        ('started', 'Started'),
        ('finished', 'Finished'),
        ('blocked', 'Blocked'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='started')
    employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employer_tasks')
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employee_tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

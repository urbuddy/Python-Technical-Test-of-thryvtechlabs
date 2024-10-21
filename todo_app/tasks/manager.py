# todo_app/managers.py
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **kwargs):
        if not phone_number:
            raise ValueError('Users must have a phone number')

        user = self.model(phone_number=phone_number, **kwargs)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, phone_number, password):
        user = self.create_user(
            phone_number=phone_number,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

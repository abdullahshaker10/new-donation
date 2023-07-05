from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from users.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    email = models.EmailField(unique=True)
    objects = CustomUserManager()
    type = models.CharField(
        max_length=100,
        choices=[("benefactor", "benefactor"), ("needy", "needy")],
        default="benefactor",
    )
    USERNAME_FIELD = "email"

from django.contrib.auth.models import AbstractUser
from django.db import models

from building_manager_app import settings


class UserModel(AbstractUser):
    USERNAME_FIELD = "email"
    email = models.EmailField(max_length=256, unique=True)
    username = models.CharField(max_length=256)
    REQUIRED_FIELDS = []


class ResetPassword(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=256, unique=True)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

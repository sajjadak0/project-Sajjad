from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    USERNAME_FIELD = "email"
    email = models.EmailField(max_length=256, unique=True)
    username = models.CharField(max_length=256, blank=True)
    REQUIRED_FIELDS = []


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

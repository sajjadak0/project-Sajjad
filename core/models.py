from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    USERNAME_FIELD = "email"
    email = models.EmailField(max_length=256, unique=True)
    username = models.CharField(max_length=256)
    REQUIRED_FIELDS = []

from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    mobile = models.CharField(max_length=11)
    email = models.EmailField(unique=True)


    # objects = CustomUserManager()
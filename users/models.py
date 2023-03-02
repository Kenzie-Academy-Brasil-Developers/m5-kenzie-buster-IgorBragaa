# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=127, unique=True)
    birthdate = models.DateField(null=True)
    last_name = models.CharField(max_length=50)
    is_employee = models.BooleanField(default=False)

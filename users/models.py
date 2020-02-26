# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    Admin = 'A'
    Parent = 'P'
    Child = 'C'
    USER_TYPE_CHOICES = [
        (Admin, 'Admin'),
        (Parent, 'Parent'),
        (Child, 'Child'),
    ]
    user_type =  models.CharField(
        max_length = 1 ,
        choices=USER_TYPE_CHOICES,
        default=Child,
    )
    score = models.IntegerField(default=0)
    arabic_name = models.CharField(max_length=200)
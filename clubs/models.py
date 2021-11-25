from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
   username = models.CharField(
       max_length=30,
       unique=True,
       validators=[RegexValidator(
           regex=r'^@\w{3,}$',
           message= 'Username must correct'
        )]
    )
    first_name = models.CharField(max_length=50,blank=False)
    last_name = models.CharField(max_length=50,blank=False)
    email = models.EmailField(unique=True,blank=False)
    bio = models.CharField(max_length=520,blank=False)

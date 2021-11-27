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
 bio = models.TextField(max_length=520,blank=False)
 LEVELS = (
   ('N', 'New to Chess'),
   ('B', 'Beginner'),
   ('I', 'Intermediate'),
   ('A', 'Advanced'),
   ('E', 'Expert'),
 )
 experience = models.CharField(max_length=1, choices=LEVELS, default='N')
 statement = models.TextField(max_length=520, blank=False)

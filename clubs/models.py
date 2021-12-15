from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
from libgravatar import Gravatar

class User(AbstractUser):
 username = models.CharField(
       max_length=30,
       unique=True,
       validators=[RegexValidator(
           regex=r'^@\w{3,}$',
           message= 'Username must correct'
        )]
    )
 LEVELS = (
   ('N', 'New to Chess'),
   ('B', 'Beginner'),
   ('I', 'Intermediate'),
   ('A', 'Advanced'),
   ('E', 'Expert'),
 )

 statement = models.TextField(max_length=520, blank=True)
 bio = models.TextField(max_length=520,blank=True)
 #experience = models.CharField(max_length=1, choices=LEVELS, default='N')

 def full_name(self):
      return f'{self.first_name} {self.last_name}'

 def gravatar(self, size=120):
        """Return a URL to the user's gravatar."""
        gravatar_object = Gravatar(self.email)
        gravatar_url = gravatar_object.get_image(size=size, default='mp')
        return gravatar_url

def mini_gravatar(self):
        """Return a URL to a miniature version of the user's gravatar."""
        return self.gravatar(size=60)


class Post(models.Model):
    """Posts by users in their clubs."""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Model options."""

        ordering = ['-created_at']

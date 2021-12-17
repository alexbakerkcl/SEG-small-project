from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from libgravatar import Gravatar


class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    experience = models.CharField(
        max_length=1,
        choices=[
            ("N", "New to Chess"),
            ("B", "Beginner"),
            ("I", "Intermediate"),
            ("A", "Advanced"),
            ("E", "Expert"),
        ],
        default="N",
    )
    statement = models.TextField(max_length=520, blank=True)
    bio = models.TextField(max_length=520, blank=True)
    followers = models.ManyToManyField(
        "self", symmetrical=False, related_name="followees"
    )

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def gravatar(self, size=120):
        """Return a URL to the user's gravatar."""
        return Gravatar(self.email).get_image(size=size, default="mp")

    def mini_gravatar(self):
        """Return a URL to a miniature version of the user's gravatar."""
        return self.gravatar(size=60)

    # def toggle_follow(self, followee):
    #     """Toggles whether self follows the given followee."""

    #     if followee == self:
    #         return
    #     if self.is_following(followee):
    #         self._unfollow(followee)
    #     else:
    #         self._follow(followee)

    def _follow(self, user):
        user.followers.add(self)

    def _unfollow(self, user):
        user.followers.remove(self)

    # def is_following(self, user):
    #     """Returns whether self follows the given user."""
    #     return user in self.followees.all()

    # def follower_count(self):
    #     """Returns the number of followers of self."""

    #     return self.followers.count()

    # def followee_count(self):
    #     """Returns the number of followees of self."""
    #    return self.followees.count()


class Post(models.Model):
    """Posts by users in their clubs."""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Model options."""

        ordering = ["-created_at"]


class Club(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=30,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^@\w{3,}$",
                message="clubname must contain more than three character",
            )
        ],
    )
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=50)


class ClubMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    level = models.CharField(
        max_length=1,
        choices=[("A", "Accept"), ("D", "Decline"), ("P", "Pending")],
        default="p",
    )

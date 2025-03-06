from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator


def _avatar_upload_to(self, filename: str) -> str:
    """
    Uploads the user avatar to the media directory.
    Args:
        filename (str): The name of the file being uploaded.

    Returns:
        str: The path to the uploaded file.
    """
    return f"users/{self.username}/avatar/{filename}"


class User(AbstractUser):
    email = models.EmailField(unique=True, null=True, blank=True)
    avatar = models.ImageField(upload_to=_avatar_upload_to, null=True, blank=True)
    github_id = models.BigIntegerField(unique=True, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    html_url = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=1024, null=True, blank=True)
    following = models.IntegerField(null=True, blank=True)
    followers = models.IntegerField(null=True, blank=True)
    public_repos = models.IntegerField(null=True, blank=True)
    private_repos = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username

from django.contrib.auth.models import AbstractUser
from django.db import models


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
    avatar = models.ImageField(upload_to=_avatar_upload_to, null=True, blank=True)
    github_id = models.BigIntegerField(unique=True, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    html_url = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    following = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers", blank=True
    )

    def __str__(self):
        return self.username

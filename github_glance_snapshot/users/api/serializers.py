from utils.models import models
from rest_framework import serializers
from requests import get
from django.core.files.base import ContentFile

User = models.USER


class UserSerializer(serializers.ModelSerializer):
    # avatar = serializers.SerializerMethodField()

    # def get_avatar(self, obj):
    #     request = self.context.get("request")
    #     if request:
    #         if obj.avatar:
    #             return request.build_absolute_uri(obj.avatar.url)
    #     return obj.avatar.url

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "get_full_name",
            "avatar",
            "github_id",
            "url",
            "html_url",
            "bio",
            "location",
            "following",
            "followers",
        )

    def create(self, validated_data):
        validated_data["github_id"] = self.initial_data["id"]
        if self.initial_data["avatar_url"]:
            validated_data["avatar"] = ContentFile(
                get(self.initial_data["avatar_url"]).content, name="avatar.png"
            )
        return super().create(validated_data)

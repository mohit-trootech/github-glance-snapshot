from utils.models import models
from rest_framework import serializers

User = models.USER


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

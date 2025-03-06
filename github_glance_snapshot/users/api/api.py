from rest_framework.views import APIView
from users.api.serializers import UserSerializer
from django.http import HttpResponse
from utils.models import models
from django.shortcuts import render
from django.template.loader import render_to_string
from utils.constants import Templates
from imgkit import from_string
from io import BytesIO
import os
import logging

os.environ["XDG_SESSION_TYPE"] = "xcb"
User = models.USER


class AuthBaseView(APIView):
    serializer_class = UserSerializer
    template_name = Templates.USER_CARD

    def get(self, request):
        user = User.objects.get(id=1)
        user_serializer = self.serializer_class(user)
        html_content = render_to_string(
            self.template_name, {"user": user_serializer.data}
        )
        breakpoint()
        try:
            from_string(
                html_content,
                "out.jpg",
            )
        except OSError as e:
            logging.error(f"wkhtmltoimage reported an error: {e}")
            return HttpResponse(
                "An error occurred while generating the image.", status=500
            )

        img = open("out.jpg", "rb").read()
        return HttpResponse(img, content_type="image/jpeg")

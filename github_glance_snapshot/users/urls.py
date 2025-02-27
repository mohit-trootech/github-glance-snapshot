from users.api.api import AuthBaseView
from django.urls import path

app_name = "users"

urlpatterns = [path("auth/", AuthBaseView.as_view(), name="auth")]

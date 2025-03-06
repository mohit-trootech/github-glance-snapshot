from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from utils.models import models

User = models.USER


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("username", "email", "get_full_name", "is_superuser")
    readonly_fields = ("id", "last_login", "date_joined", "github_id")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    fieldsets = (
        (
            None,
            {
                "fields": ["id", "github_id"],
            },
        ),
        (
            "Personal Details",
            {
                "fields": ("username", "email", "password", "first_name", "last_name"),
            },
        ),
        (
            "Github Details",
            {
                "fields": ("url", "html_url", "bio"),
            },
        ),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
        ("Groups", {"fields": ("groups", "user_permissions")}),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser")},
        ),
        (
            "Profile Image",
            {"fields": ("avatar",)},
        ),
    )
    filter_horizontal = ("groups", "user_permissions")

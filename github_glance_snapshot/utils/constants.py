from django.utils.translation import gettext_lazy as _

DD_MM_YYYY = "%d-%m-%Y"
YYYY_MM_DD = "%Y-%m-%d"


# Settings Constants
# =====================================================
class Settings:
    """Settings Constants"""

    ROOT_URLCONF = "conf.urls"
    WSGI_APPLICATION = "conf.wsgi.application"
    ASGI_APPLICATION = "conf.asgi.application"
    LANGUAGE_CODE = "en-us"
    TIME_ZONE = "Asia/Kolkata"
    USE_I18N = True
    USE_TZ = True
    STATIC_URL = "static/"
    STATIC_ROOT = "assets/"
    STATIC_FILES_DIRS = "templates/static/"
    TEMPLATES_URLS = "templates/"
    MEDIA_URL = "media/"
    MEDIA_ROOT = "media/"
    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Email Configurations
# =====================================================
class EmailConfig:
    """Email Configurations"""

    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.gmail.com"
    PORT_465 = 465
    PORT_587 = 587


# Celery Configuration
# =====================================================
class CeleryConfig:
    """Celery Configuration"""

    CELERY_BROKER_URL = "redis://localhost:6379/0"


class Templates:
    BASE_TEMPLATE = "base.html"
    USER_CARD = "users/user_card.html"


class GithubUrls:
    """Github Urls"""

    GISTS_LIST = "https://api.github.com/users/mohit-trootech/gists"
    GIST = "https://api.github.com/users/mohit-trootech/gists/{gist}"
    REPOS_LIST = "https://api.github.com/users/mohit-trootech/repos"
    REPO = "https://api.github.com/users/mohit-trootech/repos/{repo}"

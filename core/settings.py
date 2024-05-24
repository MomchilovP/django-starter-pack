import os
from pathlib import Path

from django.urls import reverse_lazy
from django.core.management.utils import get_random_secret_key
from django.utils.translation import gettext_lazy as _


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", get_random_secret_key())

ENVIRONMENT = os.environ.get("ENVIRONMENT", "production")
if ENVIRONMENT == "development":
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1", os.environ.get("EXTERNAL_HOSTNAME")]

INTERNAL_IPS = ("127.0.0.1", "localhost:8000")

INSTALLED_APPS = [
    "unfold",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "app.apps.AppConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Admin panel customization using django-unfold
# Visit: https://github.com/unfoldadmin/django-unfold

UNFOLD = {
    "SITE_TITLE": os.environ.get("SITE_TITLE", "Prod Ready Django Kit"),
    "SITE_HEADER": os.environ.get("SITE_HEADER", "Starter Pack"),
    "SITE_SYMBOL": "cloud",
    "SHOW_HISTORY": False,
    "ENVIRONMENT": "core.utils.environment_callback",
    # "LOGIN": {
    #     "image": lambda request: static("sample/login-bg.jpg"),
    #     "redirect_after": lambda request: reverse_lazy("admin:APP_MODEL_changelist"),
    # },
    "SIDEBAR": {
        "show_search": True,  # Search in applications and models names
        "show_all_applications": False,
        "navigation": [
            {
                "title": _("Navigation"),
                "separator": True,  # Top border
                "items": [
                    {
                        "title": _("Users"),
                        "icon": "person",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },
                    {
                        "title": _("Groups"),
                        "icon": "group",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                ],
            },
        ],
    },
}


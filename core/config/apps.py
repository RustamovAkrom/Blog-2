DEFAULT_APPS = [
    # Default apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
]
PROJECT_APPS = [
    # Project apps
    "apps.shared.apps.SharedConfig",
    "apps.blog.apps.BlogConfig",
    "apps.users.apps.UsersConfig",
]
THIRD_PARTY_APPS = [
    # Third party apps
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",

]
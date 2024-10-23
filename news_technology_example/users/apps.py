import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "news_technology_example.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import news_technology_example.users.signals  # noqa: F401

# -*- coding: utf-8 -*-
from django.conf import BaseSettings, settings as django_settings


class Settings(BaseSettings):

    UPDATER_NOTIFY = getattr(django_settings, "UPDATER_NOTIFY_ON_UPDATES", True)
    UPDATER_EMAILS = getattr(django_settings, "UPDATER_EMAILS", [mail for name, mail in django_settings.ADMINS])
    UPDATER_BASE_URL = getattr(django_settings, "UPDATER_BASE_URL", "https://djangoupdater.com")

settings = Settings()

# -*- coding: utf-8 -*-
from django.conf import BaseSettings, settings as django_settings


class Settings(BaseSettings):

    API_URL = "https://pyup.io/api/v1/insecure/django/"

settings = Settings()

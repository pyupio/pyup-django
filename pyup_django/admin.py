# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import json
from django.contrib import admin
from django.conf.urls import url
from django.http import HttpResponse
from django.template.loader import render_to_string
from django import VERSION
import time
from .models import Status
from .settings import settings
import requests
from packaging.specifiers import SpecifierSet


class StatusAdmin(admin.ModelAdmin):

    def has_module_permission(self, request):
        # don't display the app on the index site
        return False

    def get_urls(self):
        urls = super(StatusAdmin, self).get_urls()
        return [
            url(r'^pyup/$', self.admin_site.admin_view(self.registration_status_view),
                name="pyup"),
        ] + urls

    def is_insecure(self, version):
        r = requests.get(settings.API_URL)
        if r.status_code == 200:
            for spec_str in r.json()['insecure']:
                spec = SpecifierSet(spec_str)
                if spec.contains(version):
                    return True
        return False

    def registration_status_view(self, request):
        request.current_app = self.admin_site.name

        version = "{}.{}.{}".format(VERSION[0], VERSION[1], VERSION[2])

        insecure = self.is_insecure(version)

        data = {
            "django_version": version,
            "insecure": insecure,
        }

        template = "".join(render_to_string("insecure.html", data).splitlines())

        data["template"] = template
        data["run_again_at"] = time.time() + 60 * 60 * 24
        request.session["pyup_django"] = data
        return HttpResponse(json.dumps(data), content_type="application/json")

admin.site.register(Status, StatusAdmin)

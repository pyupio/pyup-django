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
from safety import safety
import pip


class StatusAdmin(admin.ModelAdmin):

    def has_module_permission(self, request):
        # don't display the app on the index site
        return False

    def get_urls(self):
        urls = super(StatusAdmin, self).get_urls()
        return [
            url(r'^safety/$', self.admin_site.admin_view(self.registration_status_view),
                name="safety"),
        ] + urls

    def registration_status_view(self, request):
        request.current_app = self.admin_site.name
        vulns = safety.check(packages=pip.get_installed_distributions())
        template = "".join(render_to_string("insecure.html", {"vulns": vulns}).splitlines())
        data = {
            "django_version": "{}.{}".format(VERSION[0], VERSION[1]),
            "insecure": len(vulns) > 0,
            "template": template,
            "run_again_at": time.time() + 60 * 60 * 24
        }
        request.session["safety_django"] = data
        return HttpResponse(json.dumps(data), content_type="application/json")

admin.site.register(Status, StatusAdmin)

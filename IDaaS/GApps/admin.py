from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from GApps.models import ScheduledSyncs


class ScheduledSyncsAdmin(admin.ModelAdmin):
    list_display = ['user', 'domain']

admin.site.register(ScheduledSyncs, ScheduledSyncsAdmin)
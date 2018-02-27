from django.db import models
from django.conf import settings
from datetime import datetime


class ScheduledSyncs(models.Model):
    """
    Class for representing scheduled syncs between GApps and LDAP
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True)
    domain = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True) 
    
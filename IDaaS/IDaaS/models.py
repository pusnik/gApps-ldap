# -*- coding: utf-8 -*-
# This software is distributed under the two-clause BSD license.
# Copyright (c) The django-ldapdb project

from django.conf import settings

import ldapdb.models
from ldapdb.models.fields import CharField, ImageField, IntegerField, ListField


class LdapUser(ldapdb.models.Model):
    """
    Class for representing an LDAP user entry.
    """
    # LDAP meta-data
    base_dn = settings.BASE_DN_USER
    object_classes = ['posixAccount', 'shadowAccount', 'inetOrgPerson']

    # inetOrgPerson
    first_name = CharField(db_column='givenName', verbose_name="Prime name")
    last_name = CharField("Final name", db_column='sn')
    full_name = CharField(db_column='cn')
    email = CharField(db_column='mail', unique=True)
    phone = CharField(db_column='telephoneNumber', blank=True)
    mobile_phone = CharField(db_column='mobile', blank=True)
    photo = ImageField(db_column='jpegPhoto', blank=True)

    # posixAccount
    uid = IntegerField(db_column='uidNumber', unique=True)
    group = IntegerField(db_column='gidNumber')
    gecos = CharField(db_column='gecos')
    home_directory = CharField(db_column='homeDirectory')
    login_shell = CharField(db_column='loginShell', default='/bin/bash')
    username = CharField(db_column='uid', primary_key=True)
    password = CharField(db_column='userPassword')

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.full_name


class LdapGroup(ldapdb.models.Model):
    """
    Class for representing an LDAP group entry.
    """
    # LDAP meta-data
    base_dn = settings.BASE_DN_GROUP
    object_classes = ['posixGroup']

    # posixGroup attributes
    gid = IntegerField(db_column='gidNumber', unique=True)
    name = CharField(db_column='cn', max_length=200, primary_key=True)
    usernames = ListField(db_column='memberUid')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


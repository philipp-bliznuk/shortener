# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 12:31
from __future__ import unicode_literals

from django.db import migrations


def create_admin(apps, schema_editor):
    from django.contrib.auth.models import User
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_admin)
    ]
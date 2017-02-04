# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 20:56
from __future__ import unicode_literals

from django.db import migrations


def save_alarms(apps, schema_editor):
    # Fuerzo un save para asignar los labels

    Alarm = apps.get_model("alarm", "Alarm")
    for alarm in Alarm.objects.all():
        alarm.save()


class Migration(migrations.Migration):

    dependencies = [
        ('alarm', '0002_auto_20170121_2047'),
    ]

    operations = [
        migrations.RunPython(save_alarms)
    ]
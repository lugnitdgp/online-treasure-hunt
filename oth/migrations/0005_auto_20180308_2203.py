# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-08 16:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0004_auto_20180128_1526'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notif',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]

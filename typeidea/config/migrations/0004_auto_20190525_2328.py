# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-25 15:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_auto_20190519_2347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siderbar',
            old_name='create_time',
            new_name='created_time',
        ),
    ]

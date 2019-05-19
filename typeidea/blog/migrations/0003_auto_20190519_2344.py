# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-19 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190519_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除'), (2, '草稿')], default=1, verbose_name='状态'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-19 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20180819_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expertreview',
            name='expertreview',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='userreview',
            name='review',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
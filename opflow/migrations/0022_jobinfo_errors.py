# -*- coding: utf-8 -*-
"""
# Generated by Django 1.10.6 on 2017-08-01 14:25
"""
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):
    """ Migration """

    dependencies = [
        ('zhongjing', '0021_faillog'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobinfo',
            name='errors',
            field=jsonfield.fields.JSONField(default={}),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 00:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafeteria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='titulo',
            new_name='producto',
        ),
    ]
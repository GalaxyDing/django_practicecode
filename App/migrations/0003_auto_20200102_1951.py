# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-01-02 11:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20200102_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grade',
            old_name='grade',
            new_name='grade_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='grade',
            new_name='s_grade',
        ),
    ]

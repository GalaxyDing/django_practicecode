# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-01-02 11:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='grade',
            table='grade',
        ),
        migrations.AlterModelTable(
            name='student',
            table='student',
        ),
    ]

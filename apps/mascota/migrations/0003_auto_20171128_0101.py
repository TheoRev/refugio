# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 01:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0002_auto_20171128_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='vacuna',
            field=models.ManyToManyField(blank=True, to='mascota.Vacuna'),
        ),
    ]

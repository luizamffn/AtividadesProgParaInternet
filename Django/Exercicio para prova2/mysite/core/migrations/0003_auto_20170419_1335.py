# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 16:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170418_2317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='Cep',
            new_name='cep',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='Estado',
            new_name='estado',
        ),
    ]

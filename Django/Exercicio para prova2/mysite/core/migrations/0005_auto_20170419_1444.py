# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 17:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170419_1348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fornecedor',
            old_name='Cep',
            new_name='cep',
        ),
        migrations.RenameField(
            model_name='fornecedor',
            old_name='Estado',
            new_name='estado',
        ),
    ]

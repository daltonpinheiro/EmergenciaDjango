# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-21 02:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0007_auto_20171220_2329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='ObsPiroridade',
            new_name='ObsPrioridade',
        ),
    ]

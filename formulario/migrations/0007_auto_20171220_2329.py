# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-21 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0006_delete_dimprioridade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='ObsPiroridade',
            field=models.TextField(max_length=100, verbose_name='Observação'),
        ),
    ]

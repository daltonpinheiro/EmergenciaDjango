# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-21 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0010_auto_20171221_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='HoraFimCR',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora Fim CR'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='ObsPrioridade',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Observação'),
        ),
    ]

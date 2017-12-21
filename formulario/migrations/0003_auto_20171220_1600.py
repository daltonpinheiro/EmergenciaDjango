# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-20 19:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0002_paciente_idade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='Classificador',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Classificador', to='formulario.DimClassificador', verbose_name='Classificador'),
        ),
    ]

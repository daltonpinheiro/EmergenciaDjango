# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-20 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0004_auto_20171220_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='Classificador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Classificador', to='formulario.DimClassificador', verbose_name='Classificador'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='Classificador2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Classificador2', to='formulario.DimClassificador', verbose_name='Classificador 2'),
        ),
    ]

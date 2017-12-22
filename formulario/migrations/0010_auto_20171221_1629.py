# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-21 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0009_auto_20171221_1307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dimclassificador',
            options={'ordering': ['DescClassificador']},
        ),
        migrations.AlterModelOptions(
            name='dimdiscriminador',
            options={'ordering': ['DescDiscriminador']},
        ),
        migrations.AlterModelOptions(
            name='dimfluxograma',
            options={'ordering': ['DescFluxograma']},
        ),
        migrations.AlterModelOptions(
            name='paciente',
            options={'ordering': ['Data', 'HoraChegada']},
        ),
        migrations.AlterField(
            model_name='paciente',
            name='FluxoInterno',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='Prontuario',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Prontuário'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='hora',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora'),
        ),
    ]

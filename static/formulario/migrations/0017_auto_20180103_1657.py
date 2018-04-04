# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-03 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0016_auto_20180103_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='AA',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='AA'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='Dor',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='Dor'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='ECG',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='ECG'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='Glic',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='Glic'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='Irreg',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='Irreg.'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='O2',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='c/ O2'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='PA',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='PA'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='Pulso',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='Pulso'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='Reg',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='Reg'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='SO2',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='SO2'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='Temp',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='Temp'),
        ),
    ]
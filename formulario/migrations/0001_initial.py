# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-20 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DimChegada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DescChegada', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DimClassificador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DescClassificador', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='DimDiscriminador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DescDiscriminador', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DimEspecialidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DescEspecialidade', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DimFluxograma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DescFluxograma', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DimPrioridade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DescPrioridade', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DimProcedencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DescProcedencia', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DimQueixa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DescQueixa', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HoraChegada', models.TimeField(verbose_name='Hora Chegada')),
                ('HoraInicioCR', models.TimeField(verbose_name='Hora Início CR')),
                ('Data', models.DateField(verbose_name='Data')),
                ('Prontuario', models.PositiveIntegerField(verbose_name='Prontuário')),
                ('Nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('Sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=2)),
                ('DataNascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('Regulado', models.CharField(choices=[('S', 'SIM'), ('N', 'NÃO')], max_length=1)),
                ('SemDiscriminador', models.BooleanField(verbose_name='Não')),
                ('Glic', models.CharField(blank=True, max_length=7, verbose_name='Glic')),
                ('ECG', models.CharField(blank=True, max_length=7, verbose_name='ECG')),
                ('Pulso', models.CharField(blank=True, max_length=7, verbose_name='Pulso')),
                ('Reg', models.CharField(blank=True, max_length=7, verbose_name='Reg')),
                ('Irreg', models.CharField(blank=True, max_length=7, verbose_name='Irreg.')),
                ('SO2', models.CharField(blank=True, max_length=7, verbose_name='SO2')),
                ('AA', models.CharField(blank=True, max_length=7, verbose_name='AA')),
                ('O2', models.CharField(blank=True, max_length=7, verbose_name='c/ O2')),
                ('Temp', models.CharField(blank=True, max_length=7, verbose_name='Temp')),
                ('Dor', models.CharField(blank=True, max_length=7, verbose_name='Dor')),
                ('PA', models.CharField(blank=True, max_length=7, verbose_name='PA')),
                ('prioridade', models.CharField(choices=[('VERMELHO', '1-EMERGENCIA (VERMELHO)'), ('LARANJA', '2-MUITO URGENTE (LARANJA)'), ('AMARELO', '3-URGENTE (AMARELO)'), ('VERDE', '4-POUCO URGENTE (VERDE)'), ('AZUL', '5-NÃO URGENTE (AZUL)'), ('BRANCO', '6-ELETIVO (BRANCO)')], max_length=9, verbose_name='Prioridade Clínica')),
                ('ObsPiroridade', models.CharField(max_length=100, verbose_name='Observação')),
                ('HoraFimCR', models.TimeField(verbose_name='Hora Fim CR')),
                ('prioridade2', models.CharField(choices=[('VERMELHO', '1-EMERGENCIA (VERMELHO)'), ('LARANJA', '2-MUITO URGENTE (LARANJA)'), ('AMARELO', '3-URGENTE (AMARELO)'), ('VERDE', '4-POUCO URGENTE (VERDE)'), ('AZUL', '5-NÃO URGENTE (AZUL)'), ('BRANCO', '6-ELETIVO (BRANCO)')], max_length=9, verbose_name='Prioridade Clínica2')),
                ('hora', models.TimeField(verbose_name='Hora')),
                ('HoraFimReclass', models.TimeField(verbose_name='Hora Fim da Reclassificação')),
                ('Chegada', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formulario.DimChegada')),
                ('Classificador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Classificador', to='formulario.DimClassificador', verbose_name='Classificador')),
                ('Classificador2', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Classificador2', to='formulario.DimClassificador', verbose_name='Classificador 2')),
                ('Discriminador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Discriminador', to='formulario.DimDiscriminador', verbose_name='Discriminador')),
                ('Discriminador2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Discriminador2', to='formulario.DimDiscriminador', verbose_name='Discriminador')),
                ('Especialidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formulario.DimEspecialidade')),
                ('Fluxograma', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formulario.DimFluxograma', verbose_name='Fluxograma')),
                ('Procedencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formulario.DimProcedencia', verbose_name='Procedência')),
                ('Queixa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formulario.DimQueixa')),
            ],
        ),
    ]

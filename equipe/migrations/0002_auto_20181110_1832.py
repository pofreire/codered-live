# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-10 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integrante_equipe',
            name='facebook',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='integrante_equipe',
            name='github',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='integrante_equipe',
            name='linkedin',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='integrante_equipe',
            name='twitter',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
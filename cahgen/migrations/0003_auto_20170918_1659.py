# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 16:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cahgen', '0002_auto_20170918_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardslist',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cahgen.PackProfile'),
        ),
        migrations.AlterField(
            model_name='pdf',
            name='render_spec',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cahgen.RenderSpec'),
        ),
    ]

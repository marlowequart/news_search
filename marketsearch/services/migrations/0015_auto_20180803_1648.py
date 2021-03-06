# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-03 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0014_auto_20160715_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='status',
            field=models.CharField(choices=[('G', '✓ good'), ('E', '× error'), ('C', '~ running')], default='G', max_length=1),
        ),
        migrations.AlterField(
            model_name='story',
            name='content_type',
            field=models.CharField(blank=True, choices=[('T', 'text'), ('U', 'url'), ('I', 'image')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='status',
            field=models.CharField(choices=[('N', 'New'), ('O', 'Ok'), ('E', 'Error')], default='N', max_length=1),
        ),
    ]

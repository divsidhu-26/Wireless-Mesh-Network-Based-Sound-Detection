# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-19 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('location', models.IntegerField()),
            ],
        ),
    ]
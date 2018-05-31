# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-31 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schema_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_schema', models.CharField(max_length=200)),
                ('table_name', models.CharField(max_length=100)),
                ('table_description', models.CharField(max_length=5000)),
            ],
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-24 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcontent', '0004_delete_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField()),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titre')),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='Date de publication')),
                ('logo', models.ImageField(blank=True, upload_to='uploads')),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]

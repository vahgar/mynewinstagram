# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('code', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=5)),
                ('country', models.ForeignKey(to='account.Country')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='street_address',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='account.State'),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.ForeignKey(null=True, blank=True, to='account.City'),
        ),
    ]

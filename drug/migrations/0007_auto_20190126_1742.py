# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-26 17:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drug', '0006_diseaserecord_symptomrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('search_query', models.CharField(blank=True, max_length=1000, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='diseaserecord',
            name='date',
        ),
        migrations.RemoveField(
            model_name='diseaserecord',
            name='user',
        ),
        migrations.RemoveField(
            model_name='symptomrecord',
            name='date',
        ),
        migrations.RemoveField(
            model_name='symptomrecord',
            name='user',
        ),
        migrations.AddField(
            model_name='diseaserecord',
            name='user_record',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drug.Record'),
        ),
        migrations.AddField(
            model_name='symptomrecord',
            name='user_record',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drug.Record'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-20 17:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('blog', '0019_auto_20160920_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalEmbeddedResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(max_length=255, unique=True)),
                ('external_source', models.CharField(choices=[('EN', 'Evernote')], max_length=2)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('local_resource_instance_id', models.IntegerField(default=0)),
                ('local_resource_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lrc', to='contenttypes.ContentType')),
                ('part_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='blog.ExternalNote')),
            ],
        ),
    ]

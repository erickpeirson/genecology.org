# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-17 13:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20160315_1829'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='data',
            options={'verbose_name': 'datum', 'verbose_name_plural': 'data'},
        ),
        migrations.AlterModelOptions(
            name='rdfclass',
            options={'verbose_name': 'RDF class', 'verbose_name_plural': 'RDF classes'},
        ),
        migrations.AlterModelOptions(
            name='rdfproperty',
            options={'verbose_name': 'RDF property', 'verbose_name_plural': 'RDF properties'},
        ),
        migrations.AlterModelOptions(
            name='rdfschema',
            options={'verbose_name': 'RDF schema', 'verbose_name_plural': 'RDF schemas'},
        ),
        migrations.AlterField(
            model_name='entity',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='entity',
            name='label',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='property',
            name='instance_of',
            field=models.ForeignKey(help_text='Each relation should have a formal type or property from a controlled vocabulary. If you don\'t see an appropriate option here, we chould consider loading additional vocabularies or, if absolutely necessary, creating our own. **Important** be sure to select a relationship with the appropriate domain and range! The domain should match the type of the "source" entity (e.g. Person) and the range should match the type of the "target" entity.', on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='blog.RDFProperty', verbose_name='property type'),
        ),
        migrations.AlterField(
            model_name='rdfproperty',
            name='domain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='in_domain_of', to='blog.RDFClass', verbose_name='domain'),
        ),
        migrations.AlterField(
            model_name='rdfproperty',
            name='partOf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='blog.RDFSchema', verbose_name='part of'),
        ),
        migrations.AlterField(
            model_name='rdfproperty',
            name='range',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='in_range_of', to='blog.RDFClass', verbose_name='range'),
        ),
    ]
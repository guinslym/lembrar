# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import rapidamente.models


class Migration(migrations.Migration):

    dependencies = [
        ('rapidamente', '0010_auto_20160612_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='nickname',
            field=models.CharField(unique=True, blank=True, null=True, max_length=12, help_text='Give a nickname to this url'),
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='slug',
            field=models.CharField(unique=True, max_length=10, default=rapidamente.models.get_uuid),
        ),
    ]

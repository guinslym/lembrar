# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapidamente', '0007_auto_20160612_0426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shorturl',
            name='shortened',
        ),
        migrations.AddField(
            model_name='shorturl',
            name='slug',
            field=models.CharField(max_length=10, default='s8g', unique=True),
        ),
    ]

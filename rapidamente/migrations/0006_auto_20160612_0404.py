# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapidamente', '0005_auto_20160612_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='shortened',
            field=models.CharField(default='wSQ', unique=True, max_length=10),
        ),
    ]

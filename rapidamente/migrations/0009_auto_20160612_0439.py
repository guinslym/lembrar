# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapidamente', '0008_auto_20160612_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='slug',
            field=models.CharField(max_length=10, unique=True, default='qGL'),
        ),
    ]

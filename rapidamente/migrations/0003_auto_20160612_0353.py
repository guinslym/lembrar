# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapidamente', '0002_auto_20160612_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='shortened',
            field=models.CharField(max_length=20, default='ztv5dH6x9YCL'),
        ),
    ]

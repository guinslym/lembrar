# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapidamente', '0003_auto_20160612_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='shortened',
            field=models.CharField(max_length=10, default='9WW'),
        ),
    ]

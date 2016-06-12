# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapidamente', '0006_auto_20160612_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='shortened',
            field=models.CharField(unique=True, default='oat', max_length=10),
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='url',
            field=models.URLField(help_text='i.e. http://www.yahoo.com', max_length=250),
        ),
    ]

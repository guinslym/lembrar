# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapidamente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='got_nickname',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='nickname',
            field=models.CharField(max_length=12, help_text='The alternate url name', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='shortened',
            field=models.CharField(max_length=20, default='NbtQ8YwAp2mY'),
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='website',
            field=models.URLField(max_length=8, help_text='i.e. http://www.yahoo.com'),
        ),
    ]

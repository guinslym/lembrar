# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rapidamente', '0011_auto_20160612_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='expiring_date',
            field=models.DateField(null=True, blank=True, default=datetime.datetime(2016, 7, 12, 20, 6, 7, 625773, tzinfo=utc), help_text='Select a date of Expiration. By default it is set two 1 months'),
        ),
    ]

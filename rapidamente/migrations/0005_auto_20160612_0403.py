# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapidamente', '0004_auto_20160612_0400'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shorturl',
            old_name='website',
            new_name='url',
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='nickname',
            field=models.CharField(help_text='Give a nickname to this url', max_length=12, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='shortened',
            field=models.CharField(default='Lmj', max_length=10),
        ),
    ]

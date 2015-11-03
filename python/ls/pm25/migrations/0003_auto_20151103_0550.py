# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pm25', '0002_auto_20151103_0354'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='parent',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='town',
            name='parent',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]

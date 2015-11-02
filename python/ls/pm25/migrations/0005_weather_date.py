# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pm25', '0004_weather'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='date',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]

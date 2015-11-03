# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pm25', '0003_auto_20151103_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='province',
            name='parent',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]

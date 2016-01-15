# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0008_auto_20150603_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(3000, 1, 1, 0, 0)),
        ),
    ]
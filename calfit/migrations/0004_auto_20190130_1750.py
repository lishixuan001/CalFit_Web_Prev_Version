# Generated by Django 2.0.6 on 2019-01-30 17:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calfit', '0003_record_steps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 30, 17, 50, 20, 513957)),
        ),
    ]

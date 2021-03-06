# Generated by Django 2.0.6 on 2019-02-03 08:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calfit', '0005_auto_20190130_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=None)),
                ('goal', models.IntegerField(default=0)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 3, 8, 48, 0, 463816, tzinfo=utc)),
        ),
    ]

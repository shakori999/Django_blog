# Generated by Django 3.2.8 on 2021-10-31 13:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogf', '0002_auto_20211031_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 31, 13, 41, 33, 800258, tzinfo=utc)),
        ),
    ]

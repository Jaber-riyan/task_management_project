# Generated by Django 4.2.7 on 2023-12-09 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='task_assign_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 9, 17, 5, 7, 358774)),
        ),
    ]

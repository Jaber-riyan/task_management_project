# Generated by Django 4.2.7 on 2024-02-03 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_taskmodel_is_completed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='task_assign_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

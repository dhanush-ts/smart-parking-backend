# Generated by Django 5.0.7 on 2024-09-06 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0006_tansaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tansaction',
            name='time',
        ),
        migrations.AddField(
            model_name='tansaction',
            name='cost',
            field=models.IntegerField(default=0),
        ),
    ]

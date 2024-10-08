# Generated by Django 5.0.7 on 2024-09-06 03:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0009_parking_number_plate'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumberPlate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='numberUser', to='features.user')),
            ],
        ),
        migrations.AlterField(
            model_name='parking',
            name='number_plate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='numberPlate', to='features.numberplate'),
        ),
    ]

# Generated by Django 5.0.7 on 2024-09-05 18:09

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_alter_category_no_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='address',
        ),
        migrations.RemoveField(
            model_name='category',
            name='cost_per_minute',
        ),
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='category',
            name='no_available',
        ),
        migrations.RemoveField(
            model_name='category',
            name='rating',
        ),
        migrations.CreateModel(
            name='CategoryData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('no_available', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('image', models.ImageField(upload_to='')),
                ('cost_per_minute', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='features.category')),
            ],
        ),
    ]

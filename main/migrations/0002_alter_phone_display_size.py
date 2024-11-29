# Generated by Django 5.1.3 on 2024-11-29 09:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='display_size',
            field=models.DecimalField(decimal_places=2, max_digits=2, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Display Size'),
        ),
    ]

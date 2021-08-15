# Generated by Django 3.2.6 on 2021-08-15 05:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0033_auto_20210804_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pset',
            name='clubs',
            field=models.IntegerField(blank=True, help_text='Total number of clubs that you solved (including 1♣ if feedback written)', null=True, validators=[django.core.validators.MaxValueValidator(200)], verbose_name='Total ♣ earned'),
        ),
        migrations.AlterField(
            model_name='pset',
            name='hours',
            field=models.FloatField(blank=True, help_text='Number of hours spent on this problem set', null=True, validators=[django.core.validators.MaxValueValidator(200)], verbose_name='Hours spent (estimate)'),
        ),
    ]

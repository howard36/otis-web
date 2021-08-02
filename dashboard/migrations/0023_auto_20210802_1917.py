# Generated by Django 3.2.5 on 2021-08-02 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0022_auto_20210730_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psetsubmission',
            name='clubs',
            field=models.IntegerField(help_text='Total number of clubs that you solved (including 1♣ if feedback written)', verbose_name='Total ♣ earned'),
        ),
        migrations.AlterField(
            model_name='psetsubmission',
            name='hours',
            field=models.FloatField(help_text='Number of hours spent on this problem set', verbose_name='Hours spent (estimate)'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-12 06:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rpg", "0005_achievement_show_solution"),
    ]

    operations = [
        migrations.AlterField(
            model_name="achievement",
            name="always_show_image",
            field=models.BooleanField(
                default=False,
                help_text="If enabled, always show the achievement image, even if no one earned the diamond yet.",
                verbose_name="Show Image",
            ),
        ),
        migrations.AlterField(
            model_name="achievement",
            name="show_solution",
            field=models.BooleanField(
                default=True,
                help_text="If enabled, the solution page for a diamond is available to those who have unlocked the diamond.",
                verbose_name="Show Solution",
            ),
        ),
    ]

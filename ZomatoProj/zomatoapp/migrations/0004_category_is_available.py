# Generated by Django 3.2.4 on 2024-11-13 12:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zomatoapp", "0003_auto_20241113_1807"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="is_available",
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 5.1.3 on 2024-12-10 17:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vendor", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="vendor",
            name="vendor_slug",
            field=models.SlugField(blank=True, max_length=100),
        ),
    ]

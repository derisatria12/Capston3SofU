# Generated by Django 5.1.3 on 2024-12-10 18:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vendor", "0005_vendor_vendor_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vendor",
            name="vendor_slug",
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]

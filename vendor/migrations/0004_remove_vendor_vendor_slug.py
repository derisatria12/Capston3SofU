# Generated by Django 5.1.3 on 2024-12-10 18:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("vendor", "0003_alter_vendor_vendor_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vendor",
            name="vendor_slug",
        ),
    ]

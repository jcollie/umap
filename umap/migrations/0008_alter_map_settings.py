# Generated by Django 4.1.7 on 2023-02-27 12:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("umap", "0007_auto_20190416_1757"),
    ]

    operations = [
        migrations.AlterField(
            model_name="map",
            name="settings",
            field=models.JSONField(
                blank=True, default=dict, null=True, verbose_name="settings"
            ),
        ),
    ]

# Generated by Django 2.0.5 on 2018-05-19 09:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("umap", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tilelayer",
            name="tms",
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.1.7 on 2023-05-05 18:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("umap", "0008_alter_map_settings"),
    ]

    operations = [
        migrations.CreateModel(
            name="Star",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("at", models.DateTimeField(auto_now=True)),
                (
                    "by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stars",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "map",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="umap.map"
                    ),
                ),
            ],
        ),
    ]

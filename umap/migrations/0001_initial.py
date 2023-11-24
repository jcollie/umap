# Generated by Django 2.0.5 on 2018-05-19 09:27

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import umap.fields
import umap.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="DataLayer",
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
                ("name", models.CharField(max_length=200, verbose_name="name")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="description"),
                ),
                (
                    "geojson",
                    models.FileField(
                        blank=True, null=True, upload_to=umap.models.upload_to
                    ),
                ),
                (
                    "display_on_load",
                    models.BooleanField(
                        default=False,
                        help_text="Display this layer on load.",
                        verbose_name="display on load",
                    ),
                ),
                ("rank", models.SmallIntegerField(default=0)),
            ],
            options={
                "ordering": ("rank",),
            },
        ),
        migrations.CreateModel(
            name="Licence",
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
                ("name", models.CharField(max_length=200, verbose_name="name")),
                (
                    "details",
                    models.URLField(
                        help_text="Link to a page where the licence is detailed.",
                        verbose_name="details",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Map",
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
                ("name", models.CharField(max_length=200, verbose_name="name")),
                ("slug", models.SlugField()),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="description"),
                ),
                (
                    "center",
                    django.contrib.gis.db.models.fields.PointField(
                        geography=True, srid=4326, verbose_name="center"
                    ),
                ),
                ("zoom", models.IntegerField(default=7, verbose_name="zoom")),
                (
                    "locate",
                    models.BooleanField(
                        default=False,
                        help_text="Locate user on load?",
                        verbose_name="locate",
                    ),
                ),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "edit_status",
                    models.SmallIntegerField(
                        choices=[
                            (1, "Everyone can edit"),
                            (2, "Only editors can edit"),
                            (3, "Only owner can edit"),
                        ],
                        default=3,
                        verbose_name="edit status",
                    ),
                ),
                (
                    "share_status",
                    models.SmallIntegerField(
                        choices=[
                            (1, "everyone (public)"),
                            (2, "anyone with link"),
                            (3, "editors only"),
                        ],
                        default=1,
                        verbose_name="share status",
                    ),
                ),
                (
                    "settings",
                    umap.fields.DictField(
                        blank=True, null=True, verbose_name="settings"
                    ),
                ),
                (
                    "editors",
                    models.ManyToManyField(
                        blank=True, to=settings.AUTH_USER_MODEL, verbose_name="editors"
                    ),
                ),
                (
                    "licence",
                    models.ForeignKey(
                        default=umap.models.get_default_licence,
                        help_text="Choose the map licence.",
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="umap.Licence",
                        verbose_name="licence",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="owned_maps",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="owner",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Pictogram",
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
                ("name", models.CharField(max_length=200, verbose_name="name")),
                ("attribution", models.CharField(max_length=300)),
                ("pictogram", models.ImageField(upload_to="pictogram")),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TileLayer",
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
                ("name", models.CharField(max_length=200, verbose_name="name")),
                (
                    "url_template",
                    models.CharField(
                        help_text="URL template using OSM tile format", max_length=200
                    ),
                ),
                ("minZoom", models.IntegerField(default=0)),
                ("maxZoom", models.IntegerField(default=18)),
                ("attribution", models.CharField(max_length=300)),
                (
                    "rank",
                    models.SmallIntegerField(
                        blank=True,
                        help_text="Order of the tilelayers in the edit box",
                        null=True,
                    ),
                ),
            ],
            options={
                "ordering": ("rank", "name"),
            },
        ),
        migrations.AddField(
            model_name="map",
            name="tilelayer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="maps",
                to="umap.TileLayer",
                verbose_name="background",
            ),
        ),
        migrations.AddField(
            model_name="datalayer",
            name="map",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="umap.Map"
            ),
        ),
    ]

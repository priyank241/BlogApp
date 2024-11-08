# Generated by Django 5.1.2 on 2024-11-01 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0003_comment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("slug", models.SlugField()),
            ],
            options={
                "ordering": ("title",),
            },
        ),
    ]

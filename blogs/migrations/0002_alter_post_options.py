# Generated by Django 5.1.2 on 2024-11-01 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ("-created_at",)},
        ),
    ]

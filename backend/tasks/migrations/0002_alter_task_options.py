# Generated by Django 5.1.7 on 2025-03-11 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["-created_at"]},
        ),
    ]

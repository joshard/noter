# Generated by Django 5.0.8 on 2024-10-01 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("note", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]

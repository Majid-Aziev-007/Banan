# Generated by Django 4.2.8 on 2023-12-22 19:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finance", "0002_alter_operation_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="operation",
            name="source",
            field=models.TextField(blank=True, null=True),
        ),
    ]

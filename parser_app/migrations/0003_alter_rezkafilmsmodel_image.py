# Generated by Django 5.1.6 on 2025-03-21 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0002_rezkafilmsmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rezkafilmsmodel',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.1.6 on 2025-03-11 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='trailer',
            field=models.URLField(null=True),
        ),
    ]

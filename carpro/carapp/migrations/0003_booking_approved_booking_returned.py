# Generated by Django 5.0.7 on 2024-07-26 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0002_booking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='returned',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 4.2.11 on 2024-04-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_system', '0006_remove_booking_full_name_booking_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='approval',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.11 on 2024-04-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_system', '0008_alter_booking_approval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=200),
        ),
    ]

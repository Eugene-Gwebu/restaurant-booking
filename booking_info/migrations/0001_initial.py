# Generated by Django 4.2.11 on 2024-04-24 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='Name', max_length=200)),
                ('last_name', models.CharField(default='Surname', max_length=200)),
                ('email', models.EmailField(default='example@example.com', max_length=200)),
                ('phone_number', models.CharField(blank=True, max_length=40, null=True)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

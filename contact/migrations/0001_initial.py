# Generated by Django 4.2.11 on 2024-05-11 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=200)),
                ('your_email', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('additional_comments', models.TextField(null=True)),
            ],
        ),
    ]

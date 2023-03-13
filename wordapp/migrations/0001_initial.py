# Generated by Django 4.1.7 on 2023-03-12 20:13

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default=None, max_length=50)),
                ('name', models.CharField(default=None, max_length=30)),
                ('message', models.TextField(default=None)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time', models.TimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=None, max_length=30)),
                ('plan_name', models.CharField(default=None, max_length=30)),
                ('total_file_remaining', models.IntegerField(default=0)),
                ('download_file', models.IntegerField(default=1)),
                ('upload_file', models.IntegerField(default=1)),
                ('old_file_number', models.IntegerField(default=1)),
                ('join_date', models.DateField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateField(default=datetime.datetime(2023, 4, 11, 20, 13, 35, 704825))),
            ],
        ),
        migrations.CreateModel(
            name='Savefile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=None, max_length=30)),
                ('file_content', models.TextField(default=None)),
                ('file_number', models.IntegerField(default=1)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time', models.TimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]

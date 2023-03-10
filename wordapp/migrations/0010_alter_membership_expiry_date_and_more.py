# Generated by Django 4.1.7 on 2023-03-09 20:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordapp', '0009_rename_filenumber_savefile_file_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 8, 20, 58, 40, 240931, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='savefile',
            name='file_number',
            field=models.IntegerField(default=1),
        ),
    ]
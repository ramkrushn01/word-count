# Generated by Django 4.1.7 on 2023-03-09 21:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordapp', '0010_alter_membership_expiry_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='old_file_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='membership',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 8, 21, 5, 43, 808532, tzinfo=datetime.timezone.utc)),
        ),
    ]
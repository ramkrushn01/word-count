# Generated by Django 4.1.7 on 2023-03-10 21:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordapp', '0015_alter_membership_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 9, 21, 32, 17, 42167)),
        ),
    ]

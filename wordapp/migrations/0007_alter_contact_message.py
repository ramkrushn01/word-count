# Generated by Django 4.1.7 on 2023-03-09 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordapp', '0006_alter_contact_date_alter_contact_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(default=None),
        ),
    ]

# Generated by Django 3.1.1 on 2020-10-10 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201010_0824'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='phongBooking',
            new_name='phoneBooking',
        ),
    ]

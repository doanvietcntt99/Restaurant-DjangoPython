# Generated by Django 3.1.1 on 2020-10-13 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20201013_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkInBooking',
            field=models.DateField(),
        ),
    ]

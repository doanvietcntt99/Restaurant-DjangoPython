# Generated by Django 3.1.2 on 2020-10-17 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20201017_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='statusUser',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 3.1.1 on 2020-10-10 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20201010_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('FullName', models.CharField(max_length=100)),
                ('DOBUser', models.DateField()),
                ('emailUser', models.CharField(max_length=100)),
                ('phoneUser', models.CharField(max_length=12)),
                ('avatarUser', models.ImageField(upload_to='images/users')),
                ('statusUser', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='avatarBlog',
            field=models.ImageField(upload_to='images/blogs/'),
        ),
        migrations.AlterField(
            model_name='food',
            name='avatarFood',
            field=models.ImageField(upload_to='images/foods/'),
        ),
        migrations.AlterField(
            model_name='masterchef',
            name='avatarChef',
            field=models.ImageField(upload_to='images/chefs'),
        ),
    ]

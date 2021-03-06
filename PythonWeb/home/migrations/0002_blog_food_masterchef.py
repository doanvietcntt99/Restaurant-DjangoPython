# Generated by Django 3.1.1 on 2020-10-10 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameBlog', models.CharField(max_length=100)),
                ('posterBlog', models.CharField(max_length=100)),
                ('titleBlog', models.CharField(max_length=100)),
                ('contentBlog', models.CharField(max_length=100)),
                ('avatarBlog', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameFood', models.CharField(max_length=100)),
                ('ingredientFood', models.CharField(max_length=100)),
                ('payFood', models.CharField(max_length=100)),
                ('avatarFood', models.CharField(max_length=100)),
                ('nameTypeFood', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MasterChef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameChef', models.CharField(max_length=100)),
                ('positionChef', models.CharField(max_length=100)),
                ('selfIntroduceChef', models.CharField(max_length=100)),
                ('avatarChef', models.CharField(max_length=100)),
            ],
        ),
    ]

# Generated by Django 3.2.18 on 2023-04-07 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=30, unique=True, verbose_name='category'),
        ),
    ]
# Generated by Django 3.2.18 on 2023-04-12 07:31

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20230412_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='accounts.User/'),
        ),
    ]

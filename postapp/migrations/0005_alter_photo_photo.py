# Generated by Django 4.2 on 2023-05-18 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0004_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
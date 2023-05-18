# Generated by Django 4.2 on 2023-05-18 01:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField(blank=True, null=True)),
                ('writedate', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('reward', models.IntegerField()),
                ('user', models.ForeignKey(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'post',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('photo_id', models.AutoField(primary_key=True, serialize=False)),
                ('src', models.CharField(blank=True, max_length=100, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='postapp.post')),
            ],
            options={
                'db_table': 'photo',
                'managed': True,
            },
        ),
    ]
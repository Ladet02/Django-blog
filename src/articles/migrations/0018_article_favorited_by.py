# Generated by Django 3.0 on 2019-12-19 14:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0017_auto_20191218_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='favorited_by',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]

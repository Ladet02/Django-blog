# Generated by Django 3.0 on 2019-12-10 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20191210_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.CharField(default='', max_length=500),
        ),
    ]

# Generated by Django 3.0 on 2019-12-19 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0018_article_favorited_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='favorited_by',
        ),
    ]

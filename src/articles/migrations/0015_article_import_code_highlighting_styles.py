# Generated by Django 3.0 on 2019-12-13 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_remove_article_comment_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='import_code_highlighting_styles',
            field=models.BooleanField(default=False),
        ),
    ]

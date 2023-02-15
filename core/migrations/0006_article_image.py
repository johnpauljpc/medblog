# Generated by Django 4.0.6 on 2023-02-13 10:59

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_articleseries_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='images/favicon.PNG', max_length=200, upload_to=core.models.Article.image_upload_to),
        ),
    ]
# Generated by Django 4.0.6 on 2023-02-14 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_article_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='series',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='core.articleseries'),
        ),
    ]

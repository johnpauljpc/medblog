# Generated by Django 4.0.6 on 2023-02-12 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_customuser_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='picture',
        ),
    ]

# Generated by Django 4.0.6 on 2023-02-12 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='picture',
            field=models.ImageField(upload_to='images/profile_pics'),
        ),
    ]
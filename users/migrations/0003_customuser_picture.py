# Generated by Django 4.0.6 on 2023-02-12 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_decription_customuser_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='picture',
            field=models.ImageField(default='images/profile.jpg', upload_to='images/profile_pics'),
        ),
    ]

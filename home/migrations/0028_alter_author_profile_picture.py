# Generated by Django 4.2.2 on 2023-07-08 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_alter_author_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', upload_to='profilepics'),
        ),
    ]

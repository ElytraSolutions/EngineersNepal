# Generated by Django 4.2.2 on 2023-07-03 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_post_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='language',
        ),
    ]
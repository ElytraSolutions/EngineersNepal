# Generated by Django 4.2.2 on 2023-08-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
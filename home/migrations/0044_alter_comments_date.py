# Generated by Django 4.2.2 on 2023-08-21 11:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0043_alter_comments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 21, 11, 2, 11, 883905)),
        ),
    ]
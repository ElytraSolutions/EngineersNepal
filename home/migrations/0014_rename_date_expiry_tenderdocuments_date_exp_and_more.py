# Generated by Django 4.2.2 on 2023-06-29 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_tenderdocuments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tenderdocuments',
            old_name='date_expiry',
            new_name='date_exp',
        ),
        migrations.AlterField(
            model_name='tenderdocuments',
            name='title',
            field=models.CharField(max_length=400),
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-03 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_remove_post_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateField(blank=True, null=True),
        ),
    ]

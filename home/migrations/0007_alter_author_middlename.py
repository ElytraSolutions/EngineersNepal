# Generated by Django 4.2.2 on 2023-06-26 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_author_slug_remove_post_categories_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='middlename',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
    ]

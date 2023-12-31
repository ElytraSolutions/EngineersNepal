# Generated by Django 4.2.2 on 2023-06-27 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_author_middlename'),
    ]

    operations = [
        migrations.CreateModel(
            name='advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='post_ads')),
                ('link', models.URLField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_expiry', models.DateField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, unique=True),
        ),
    ]

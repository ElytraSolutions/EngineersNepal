# Generated by Django 4.2.2 on 2023-06-29 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_vacancy_videos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='status',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='address',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
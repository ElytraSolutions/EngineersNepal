# Generated by Django 4.2.2 on 2023-06-29 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_category_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_expiry', models.DateField()),
                ('status', models.BooleanField(default=True)),
                ('place', models.CharField(choices=[('Onsite', 'Onsite'), ('Remote', 'Remote')], max_length=10)),
                ('worktime', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=100)),
                ('link', models.URLField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-03 10:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_epapers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epapers',
            name='epaper_pdf',
            field=models.FileField(upload_to='epapers', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]

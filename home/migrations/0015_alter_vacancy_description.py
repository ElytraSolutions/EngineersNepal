# Generated by Django 4.2.2 on 2023-07-02 10:09

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_rename_date_expiry_tenderdocuments_date_exp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]

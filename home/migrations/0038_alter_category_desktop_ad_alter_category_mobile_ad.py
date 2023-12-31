# Generated by Django 4.2.2 on 2023-07-30 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_category_desktop_ad_category_mobile_ad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='desktop_ad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='destop_ad', to='home.advertisement'),
        ),
        migrations.AlterField(
            model_name='category',
            name='mobile_ad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mobile_ad', to='home.advertisement'),
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_post_breakingthumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='grid',
            field=models.CharField(choices=[('gridone', 'gridone'), ('gridtwo', 'gridtwo')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='post_thumbs/default.jpg', upload_to='post_thumbs'),
        ),
    ]

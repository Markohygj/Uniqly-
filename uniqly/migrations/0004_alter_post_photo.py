# Generated by Django 5.1.4 on 2025-02-23 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniqly', '0003_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='Image'),
        ),
    ]

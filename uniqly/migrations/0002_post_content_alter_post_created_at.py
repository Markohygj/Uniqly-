# Generated by Django 5.1.4 on 2025-02-16 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniqly', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

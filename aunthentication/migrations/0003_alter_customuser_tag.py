# Generated by Django 5.1.4 on 2025-02-05 16:28

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aunthentication', '0002_customuser_avatar_customuser_bio_customuser_hat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='tag',
            field=models.CharField(default=uuid.uuid4, max_length=20, unique=True),
        ),
    ]

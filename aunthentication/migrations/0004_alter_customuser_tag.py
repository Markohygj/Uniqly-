# Generated by Django 5.1.4 on 2025-02-05 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aunthentication', '0003_alter_customuser_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='tag',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]

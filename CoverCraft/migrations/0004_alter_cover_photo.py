# Generated by Django 5.0.7 on 2024-10-19 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoverCraft', '0003_glass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cover',
            name='photo',
            field=models.ImageField(upload_to='images'),
        ),
    ]

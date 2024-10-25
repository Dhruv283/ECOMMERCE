# Generated by Django 5.0.7 on 2024-10-19 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoverCraft', '0002_skin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(choices=[('iPhone 6', 'iPhone 6'), ('iPhone 6 Plus', 'iPhone 6 Plus'), ('iPhone 6S', 'iPhone 6S'), ('iPhone 6S Plus', 'iPhone 6S Plus'), ('iPhone 7', 'iPhone 7'), ('iPhone 7 Plus', 'iPhone 7 Plus'), ('iPhone 8', 'iPhone 8'), ('iPhone 8 Plus', 'iPhone 8 Plus'), ('iPhone X', 'iPhone X'), ('iPhone XR', 'iPhone XR'), ('iPhone XS', 'iPhone XS'), ('iPhone XS Max', 'iPhone XS Max'), ('iPhone 11', 'iPhone 11'), ('iPhone 11 Pro', 'iPhone 11 Pro'), ('iPhone 11 Pro Max', 'iPhone 11 Pro Max'), ('iPhone 12', 'iPhone 12'), ('iPhone 12 Mini', 'iPhone 12 Mini'), ('iPhone 12 Pro', 'iPhone 12 Pro'), ('iPhone 12 Pro Max', 'iPhone 12 Pro Max'), ('iPhone 13', 'iPhone 13'), ('iPhone 13 Mini', 'iPhone 13 Mini'), ('iPhone 13 Pro', 'iPhone 13 Pro'), ('iPhone 13 Pro Max', 'iPhone 13 Pro Max'), ('iPhone 14', 'iPhone 14'), ('iPhone 14 Plus', 'iPhone 14 Plus'), ('iPhone 14 Pro', 'iPhone 14 Pro'), ('iPhone 14 Pro Max', 'iPhone 14 Pro Max'), ('iPhone 15', 'iPhone 15'), ('iPhone 15 Plus', 'iPhone 15 Plus'), ('iPhone 15 Pro', 'iPhone 15 Pro'), ('iPhone 15 Pro Max', 'iPhone 15 Pro Max'), ('iPhone 16', 'iPhone 16'), ('iPhone 16+', 'iPhone 16+')], default='iphone 16', max_length=25)),
                ('price', models.IntegerField(default=10)),
                ('desc', models.TextField(max_length=100)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
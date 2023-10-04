# Generated by Django 4.2.4 on 2023-08-30 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=300)),
                ('price', models.CharField(max_length=20)),
                ('product_id', models.CharField(max_length=30, unique=True)),
                ('img', models.ImageField(upload_to='images/')),
                ('category', models.CharField(max_length=30)),
            ],
        ),
    ]

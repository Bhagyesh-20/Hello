# Generated by Django 5.0.3 on 2024-03-17 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_products'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]

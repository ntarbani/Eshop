# Generated by Django 3.2.4 on 2021-06-20 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='Customer',
            new_name='customer',
        ),
    ]

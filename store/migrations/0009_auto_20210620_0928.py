# Generated by Django 3.2.4 on 2021-06-20 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_rename_customer_orders_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=12),
        ),
    ]

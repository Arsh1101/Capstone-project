# Generated by Django 4.2.6 on 2023-10-10 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_inventory_alter_booking_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]

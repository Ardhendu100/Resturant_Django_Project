# Generated by Django 4.0.2 on 2022-03-14 17:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_order_address_order_email_order_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='landmark',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 3, 14, 22, 35, 26, 602841)),
        ),
    ]
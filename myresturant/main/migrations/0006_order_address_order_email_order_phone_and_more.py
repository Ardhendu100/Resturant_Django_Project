# Generated by Django 4.0.2 on 2022-03-14 17:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_order_customer_alter_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default=' ', max_length=254),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default=' ', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 3, 14, 22, 34, 20, 542745)),
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-15 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_order_customer_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 3, 15, 19, 40, 39, 787277)),
        ),
    ]

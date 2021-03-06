# Generated by Django 4.0.2 on 2022-03-14 16:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_customersignup_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('date', models.DateField(default=datetime.datetime(2022, 3, 14, 22, 26, 49, 498810))),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.fooditem')),
            ],
        ),
    ]

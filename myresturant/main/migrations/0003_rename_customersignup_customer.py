# Generated by Django 4.0.2 on 2022-03-03 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_customersignup'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomerSignup',
            new_name='Customer',
        ),
    ]
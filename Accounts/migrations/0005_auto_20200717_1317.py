# Generated by Django 3.0 on 2020-07-17 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_auto_20200716_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]

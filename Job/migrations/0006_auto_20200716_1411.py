# Generated by Django 3.0.8 on 2020-07-16 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0005_apply_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]

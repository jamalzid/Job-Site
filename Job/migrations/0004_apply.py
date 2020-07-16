# Generated by Django 3.0.8 on 2020-07-16 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0003_job_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('cv', models.FileField(upload_to='media/cv/')),
                ('letter', models.TextField()),
            ],
        ),
    ]
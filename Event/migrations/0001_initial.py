# Generated by Django 3.2.9 on 2021-12-12 22:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('text', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='Event')),
            ],
        ),
    ]
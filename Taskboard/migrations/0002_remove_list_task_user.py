# Generated by Django 3.2.9 on 2021-12-21 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Taskboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list_task',
            name='user',
        ),
    ]

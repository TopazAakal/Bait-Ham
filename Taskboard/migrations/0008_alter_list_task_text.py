# Generated by Django 3.2.9 on 2022-01-02 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taskboard', '0007_delete_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list_task',
            name='text',
            field=models.TextField(max_length=5000),
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-29 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adopter', '0004_merge_0003_alter_article_title_0003_delete_reports'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='articles',
        ),
        migrations.DeleteModel(
            name='Reports',
        ),
    ]

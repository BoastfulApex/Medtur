# Generated by Django 4.0.3 on 2022-04-15 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medturApp', '0009_news_stories_specialty'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Specialty',
            new_name='Specialist',
        ),
    ]
# Generated by Django 4.0.3 on 2022-04-20 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medturApp', '0010_rename_specialty_specialist'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinics',
            name='booking',
            field=models.URLField(max_length=500, null=True),
        ),
    ]
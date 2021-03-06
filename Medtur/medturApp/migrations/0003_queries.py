# Generated by Django 4.0.3 on 2022-04-12 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medturApp', '0002_services_clinics_close_date_clinics_open_date_tours'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('query', models.TextField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]

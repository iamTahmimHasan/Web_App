# Generated by Django 3.1.7 on 2021-04-10 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20210325_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmploymentCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_image', models.ImageField(upload_to='Employment_Country')),
                ('country_name', models.CharField(max_length=50)),
                ('country_short_description', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Employment Country',
                'verbose_name_plural': 'Employment Countrys',
            },
        ),
        migrations.CreateModel(
            name='StudyCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_image', models.ImageField(upload_to='Study_Country')),
                ('country_name', models.CharField(max_length=50)),
                ('country_short_description', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Study Country',
                'verbose_name_plural': 'Study Countrys',
            },
        ),
        migrations.CreateModel(
            name='TravelCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_image', models.ImageField(upload_to='Travel_Country')),
                ('country_name', models.CharField(max_length=50)),
                ('country_short_description', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Travel Country',
                'verbose_name_plural': 'Travel Countrys',
            },
        ),
    ]

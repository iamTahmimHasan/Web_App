# Generated by Django 3.1.6 on 2021-03-25 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_logo', models.ImageField(upload_to='company_logo', verbose_name='Company Logo')),
                ('company_description', models.CharField(max_length=155, verbose_name='Company Description For Meta Details')),
                ('company_keywords', models.CharField(default='abc, xyz, alpha,', max_length=160, verbose_name='Company keywords For Meta Details')),
            ],
        ),
    ]

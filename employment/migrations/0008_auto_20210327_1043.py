# Generated by Django 3.1.6 on 2021-03-27 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0007_auto_20210325_1746'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepageleftside',
            options={'verbose_name': 'Home Page Left Side Media', 'verbose_name_plural': 'Home Page Side Medias'},
        ),
        migrations.AlterField(
            model_name='homepageleftside',
            name='External_video_Url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Upload Video Url Via (Youtube/Others)'),
        ),
    ]

# Generated by Django 3.1.6 on 2021-03-27 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0008_auto_20210327_1043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepageleftside',
            old_name='External_video_Url',
            new_name='external_video_Url',
        ),
    ]

# Generated by Django 2.0.5 on 2019-09-23 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20190923_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='User_profile',
        ),
    ]

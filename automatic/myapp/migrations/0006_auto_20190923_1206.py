# Generated by Django 2.0.5 on 2019-09-23 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20190923_1204'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permission',
            options={'managed': True, 'permissions': (('menu_slowquery', '菜单 慢查日志'), ('menu_binlog2sql', '菜单 Binlog2SQL'), ('menu_pollingreport', '菜单 巡检报告'), ('menu_principles', '菜单 设计规范'))},
        ),
    ]

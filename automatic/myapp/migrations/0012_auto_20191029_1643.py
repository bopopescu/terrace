# Generated by Django 2.0.5 on 2019-10-29 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20191029_1631'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='query_log',
            options={'verbose_name': '查询日志', 'verbose_name_plural': '查询日志'},
        ),
        migrations.AddField(
            model_name='query_log',
            name='instance_name',
            field=models.CharField(default=1, max_length=50, verbose_name='实例名称'),
            preserve_default=False,
        ),
    ]

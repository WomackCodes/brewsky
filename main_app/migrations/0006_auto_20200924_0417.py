# Generated by Django 3.1.1 on 2020-09-24 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20200922_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brewery',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='brewery',
            name='longitude',
        ),
    ]
# Generated by Django 3.1 on 2021-01-17 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professors', '0002_auto_20210117_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='is_checked',
        ),
    ]
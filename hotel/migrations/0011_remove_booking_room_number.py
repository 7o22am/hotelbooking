# Generated by Django 2.2.7 on 2019-12-17 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0010_auto_20191217_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='room_number',
        ),
    ]

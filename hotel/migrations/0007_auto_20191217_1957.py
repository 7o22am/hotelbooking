# Generated by Django 2.2.7 on 2019-12-17 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_auto_20191217_0426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='Number of days',
            new_name='days',
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]

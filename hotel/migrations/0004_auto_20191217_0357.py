# Generated by Django 2.2.7 on 2019-12-17 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_auto_20191217_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='days',
            field=models.IntegerField(verbose_name=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='roomnumber',
            field=models.IntegerField(verbose_name=0),
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-27 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_slot_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot_booking',
            name='end_time',
            field=models.DateTimeField(unique=True),
        ),
        migrations.AlterField(
            model_name='slot_booking',
            name='start_time',
            field=models.DateTimeField(unique=True),
        ),
    ]
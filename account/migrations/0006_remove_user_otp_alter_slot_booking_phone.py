# Generated by Django 4.1.2 on 2022-11-28 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_slot_booking_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='otp',
        ),
        migrations.AlterField(
            model_name='slot_booking',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]

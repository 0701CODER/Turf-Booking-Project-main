# Generated by Django 4.1.2 on 2022-11-28 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_slot_booking_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot_booking',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

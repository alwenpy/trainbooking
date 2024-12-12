# Generated by Django 5.1.4 on 2024-12-12 09:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='booking',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='app.booking'),
        ),
        migrations.AddField(
            model_name='seat',
            name='row',
            field=models.CharField(default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='booking',
            name='seat_numbers',
            field=models.ManyToManyField(related_name='bookings', to='app.seat'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seat_number',
            field=models.IntegerField(),
        ),
    ]

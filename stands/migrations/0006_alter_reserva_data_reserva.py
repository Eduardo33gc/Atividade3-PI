# Generated by Django 4.2.5 on 2023-09-20 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stands', '0005_reserva_data_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='data_reserva',
            field=models.DateField(auto_now_add=True),
        ),
    ]

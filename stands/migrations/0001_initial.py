# Generated by Django 3.2.21 on 2023-09-21 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacao', models.CharField(max_length=200, verbose_name='Localização')),
                ('valor', models.FloatField(verbose_name='Valor')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=200, verbose_name='Nome da empresa')),
                ('cnpj', models.CharField(max_length=14, verbose_name='CNPJ')),
                ('categoria_empresa', models.CharField(choices=[('telecomunicação', 'Telecomunicação'), ('fast-food', 'Fast-Food'), ('marketing', 'Marketing'), ('cultura', 'Cultura')], max_length=200, verbose_name='Categoria da empresa')),
                ('quitado', models.BooleanField(default=False)),
                ('data_reserva', models.DateField(auto_now_add=True)),
                ('stand', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stands.stand')),
            ],
        ),
    ]

from django.db import models

# Create your models here.

class Stand(models.Model):
    localizacao = models.CharField(max_length=200, verbose_name='Localização')
    valor = models.FloatField(verbose_name='Valor')

    def __str__(self):
        return self.localizacao


class Reserva(models.Model):
    CATEGORIA = (
        ('telecomunicação', 'Telecomunicação'),
        ('fast-food', 'Fast-Food'),
        ('marketing', 'Marketing'),
        ('cultura', 'Cultura')
    )
    nome_empresa = models.CharField(max_length=200, verbose_name='Nome da empresa')
    cnpj = models.CharField(max_length=14, verbose_name='CNPJ')
    categoria_empresa = models.CharField(max_length=200, choices=CATEGORIA, verbose_name='Categoria da empresa')
    quitado = models.BooleanField(default=False)
    stand = models.OneToOneField(Stand,on_delete=models.CASCADE)
    data_reserva = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome_empresa


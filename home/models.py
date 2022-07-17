from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone



class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    endereco = models.CharField(max_length=120)
    complemento = models.CharField(max_length=120)
    cep =  models.CharField(max_length=12)
    telefone = models.CharField(max_length=12)
    observacao = models.TextField(blank=True)

    def __str__(self):
        return self.nome



class Produto(models.Model):
    nome = models.CharField(max_length=128)
    carro = models.CharField(max_length=128)
    ano = models.CharField(max_length=128)
    lado = models.CharField(max_length=128)
    vendas = models.ManyToManyField(Pessoa, through='Venda')
    obs = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    placa = models.CharField(max_length=50)
    carro = models.CharField(max_length=128)
    valor_peca = models.CharField(max_length=12 )
    obs = models.TextField(blank=True)
    sim = models.BooleanField( default=True, verbose_name='pago')
    nao = models.BooleanField('Pendente', default=False )


    def __str__(self):
        return self.placa

class Estoque4peca(models.Model):
    produto = models.CharField(max_length=120)
    motorista = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    passageiro = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    assento_esquerdo = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    assento_direito = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    quantidade_em_estoque = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    estoque_minimo = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    obs = models.TextField(blank=True)

    def __str__(self, ):
        return self.produto


class Estoque1peca(models.Model):
    produto = models.CharField(max_length=110)
    quantidade_em_estoque = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    estoque_minimo = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    obs = models.TextField(blank=True)

    def __str__(self, ):
        return self.produto




from django.db import models


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=255, null=True, blank=True)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=10, null=True, blank=True)
    estoque = models.IntegerField('Quantidade em Estoque', null=True)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=255, null=True)
    sobrenome = models.CharField('Sobrenome', max_length=255, null=True)
    email = models.EmailField('Email', max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.nome } {self.sobrenome}'

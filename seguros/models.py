import datetime
from datetime import datetime
from unittest.util import _MAX_LENGTH

from django.db import models
from django.utils.timezone import timezone

# Create your models here.

class SeguroViagem(models.Model):
    nome = models.CharField(max_length=60)
    telefone = models.CharField(max_length=25)
    email = models.EmailField()
    tipo_viagem = models.CharField(max_length=15)
    origem = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    meio_transporte = models.CharField(max_length=25)
    motivo_viagem = models.CharField(max_length=10)
    data_ida = models.DateField(null=True)
    data_volta = models.DateField(null=True)
    viajantes_ate_64 = models.IntegerField(null=True)
    viajantes_65_mais = models.IntegerField(null=True)
    mensagem = models.TextField()
    comentario_gelo = models.CharField(max_length=2000, default="", blank=True)
    data_envio = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Seguro Viagem"
        verbose_name_plural = "Seguro Viagem"

class SeguroAuto(models.Model):
    nome = models.CharField(max_length=60)
    telefone = models.CharField(max_length=25)
    email = models.EmailField()
    mensagem = models.TextField()
    comentario_gelo = models.CharField(max_length=2000, default="", blank=True)
    data_envio = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Seguro Auto"
        verbose_name_plural = "Seguro Auto"

class SeguroCasa(models.Model):
    nome = models.CharField(max_length=60)
    telefone = models.CharField(max_length=25)
    email = models.EmailField()
    mensagem = models.TextField()
    comentario_gelo = models.CharField(max_length=2000, default="", blank=True)
    data_envio = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Seguro Residencial"
        verbose_name_plural = "Seguro Residencial"

class SeguroEmpresa(models.Model):
    nome = models.CharField(max_length=60)
    telefone = models.CharField(max_length=25)
    email = models.EmailField()
    mensagem = models.TextField()
    comentario_gelo = models.CharField(max_length=2000, default="", blank=True)
    data_envio = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Seguro Empresarial"
        verbose_name_plural = "Seguro Empresarial"    

class SeguroVida(models.Model):
    nome = models.CharField(max_length=60)
    telefone = models.CharField(max_length=25)
    email = models.EmailField()
    mensagem = models.TextField()
    comentario_gelo = models.CharField(max_length=2000, default="", blank=True)
    data_envio = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Seguro Vida"
        verbose_name_plural = "Seguro Vida"    

class Contato(models.Model):
    nome = models.CharField(max_length=60)
    telefone = models.CharField(max_length=25)
    email = models.EmailField()
    mensagem = models.TextField()
    comentario_gelo = models.CharField(max_length=2000, default="", blank=True)
    data_envio = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contato"

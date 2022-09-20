from msilib.schema import MoveFile
from turtle import width

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django import forms
from django.forms import ModelForm

from .models import (Contato, SeguroAuto, SeguroCasa, SeguroEmpresa,
                     SeguroViagem, SeguroVida)


class ContatoForm(ModelForm):
    nome = forms.CharField(max_length=60)
    telefone = forms.CharField(max_length=25)
    email = forms.EmailField()
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    mensagem = forms.CharField()

    class Meta:
        model = Contato
        fields = ['nome','telefone','email', 'mensagem']

class SeguroViagemForm(ModelForm):
    nome = forms.CharField(max_length=60)
    telefone = forms.CharField(max_length=25)
    email = forms.EmailField()
    captcha_viagem = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    tipo_viagem = forms.CharField(max_length=15)
    origem = forms.CharField(max_length=50)
    destino = forms.CharField(max_length=50)
    meio_transporte = forms.CharField(max_length=25)
    motivo_viagem = forms.CharField(max_length=10)
    data_ida = forms.DateField()
    data_volta = forms.DateField()
    viajantes_ate_64 = forms.IntegerField()
    viajantes_65_mais = forms.IntegerField()
    mensagem = forms.CharField()
    class Meta:
        model = SeguroViagem
        fields = ['nome','telefone','email', 
        'tipo_viagem', 'origem', 'destino', 
        'meio_transporte', 'motivo_viagem', 'data_ida', 
        'data_volta', 'viajantes_ate_64', 'viajantes_65_mais', 'mensagem']

class SeguroAutoForm(ModelForm):
    nome = forms.CharField(max_length=60)
    telefone = forms.CharField(max_length=25)
    email = forms.EmailField()
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    mensagem = forms.CharField()
    class Meta:
        model = SeguroAuto
        fields = ['nome','telefone','email', 'mensagem']

class SeguroCasaForm(ModelForm):
    nome = forms.CharField(max_length=60)
    telefone = forms.CharField(max_length=25)
    email = forms.EmailField()
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    mensagem = forms.CharField()
    class Meta:
        model = SeguroCasa
        fields = ['nome','telefone','email', 'mensagem']

class SeguroEmpresaForm(ModelForm):
    nome = forms.CharField(max_length=60)
    telefone = forms.CharField(max_length=25)
    email = forms.EmailField()
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    mensagem = forms.CharField()
    class Meta:
        model = SeguroEmpresa
        fields = ['nome','telefone','email', 'mensagem']

class SeguroVidaForm(ModelForm):
    nome = forms.CharField(max_length=60)
    telefone = forms.CharField(max_length=25)
    email = forms.EmailField()
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    mensagem = forms.CharField()
    class Meta:
        model = SeguroVida
        fields = ['nome','telefone','email', 'mensagem']

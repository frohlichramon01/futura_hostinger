from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import (ContatoForm, SeguroAutoForm, SeguroCasaForm,
                    SeguroEmpresaForm, SeguroViagemForm, SeguroVidaForm)

# Create your views here.

def home(request):
    return render(request, 'seguros/pages/home.html')

def sobre(request):
    return render(request, 'seguros/pages/sobre.html')

def auto(request):
    if request.method == "POST":
        form = SeguroAutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Dados enviados com sucesso. Aguarde que entraremos em contato!")
            return render(request, 'seguros/pages/auto.html', {'form':SeguroAutoForm})
        else:
            messages.error(request, "Dados ou verificação incorretos.")
            return render(request, 'seguros/pages/auto.html', {'form':SeguroAutoForm})
                
    else:return render(request, 'seguros/pages/auto.html', {'form':SeguroAutoForm})
    
def vida(request):
    if request.method == "POST":
        form = SeguroVidaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Dados enviados com sucesso. Aguarde que entraremos em contato!")
            return render(request, 'seguros/pages/vida.html', {'form':SeguroVidaForm})
        else:
            messages.error(request, "Dados ou verificação incorretos.")
            return render(request, 'seguros/pages/vida.html', {'form':SeguroVidaForm})
                
    else:return render(request, 'seguros/pages/vida.html', {'form':SeguroVidaForm})

def casa(request):
    if request.method == "POST":
        form = SeguroCasaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Dados enviados com sucesso. Aguarde que entraremos em contato!")
            return render(request, 'seguros/pages/casa.html', {'form':SeguroCasaForm})
        else:
            messages.error(request, "Dados ou verificação incorretos.")
            return render(request, 'seguros/pages/casa.html', {'form':SeguroCasaForm})
                
    else:return render(request, 'seguros/pages/casa.html', {'form':SeguroCasaForm})

def empresa(request):
    if request.method == "POST":
        form = SeguroEmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Dados enviados com sucesso. Aguarde que entraremos em contato!")
            return render(request, 'seguros/pages/empresa.html', {'form':SeguroEmpresaForm})
        else:
            messages.error(request, "Dados ou verificação incorretos.")
            return render(request, 'seguros/pages/empresa.html', {'form':SeguroEmpresaForm})
                
    else:return render(request, 'seguros/pages/empresa.html', {'form':SeguroEmpresaForm})

def contato(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Dados enviados com sucesso. Aguarde que entraremos em contato!")
            return render(request, 'seguros/pages/contato.html', {'form':ContatoForm})
        else:
            messages.error(request, "Dados ou verificação incorretos.")
            return render(request, 'seguros/pages/contato.html', {'form':ContatoForm})
                
    else:return render(request, 'seguros/pages/contato.html', {'form':ContatoForm})

def viagem(request):
    if request.method == "POST":
        form = SeguroViagemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Dados enviados com sucesso. Aguarde que entraremos em contato!")
            return render(request, 'seguros/pages/viagem.html', {'form':SeguroViagemForm})
        else:
            messages.error(request, "Dados ou verificação incorretos.")
            return render(request, 'seguros/pages/viagem.html', {'form':SeguroViagemForm})
                
    else:return render(request, 'seguros/pages/viagem.html', {'form':SeguroViagemForm})

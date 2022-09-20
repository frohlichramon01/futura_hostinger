from django.contrib import admin

from seguros.models import (Contato, SeguroAuto, SeguroCasa, SeguroEmpresa,
                            SeguroViagem, SeguroVida)

# Register your models here.

class SeguroViagemAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    list_display = ['nome', 'telefone', 'email', 'data_envio','tipo_viagem', 'origem', 'destino', 'meio_transporte', 'motivo_viagem', 'data_ida', 'data_volta', 'viajantes_ate_64', 'viajantes_65_mais']
    list_filter = ['data_envio']

    def download_csv(self, request, queryset):
        import csv
        from io import StringIO

        from django.http import HttpResponse
        
        f = StringIO()
        writer = csv.writer(f)
        writer.writerow(["nome","telefone","email","data_envio","tipo_viagem", "origem", "destino", "meio_transporte", "motivo_viagem", "data_ida", "data_volta", "viajantes_ate_64", "viajantes_65_mais", "comentario_gelo"])

        for s in queryset:
            writer.writerow([s.nome, s.telefone, s.email, s.data_envio,
            s.tipo_viagem, s.origem, s.destino, s.meio_transporte,
            s.motivo_viagem, s.data_ida, s.data_volta, s.viajantes_ate_64,
            s.viajantes_65_mais, s.comentario_gelo])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Planilha_Seguro_Viagem.csv'
        return response

    download_csv.short_description = "Baixar planilha(CSV) dos itens selecionados."

class SeguroAutoAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    list_display = ['nome', 'telefone', 'email', 'data_envio']
    list_filter = ['data_envio', 'nome']

    def download_csv(self, request, queryset):
        import csv
        from io import StringIO

        from django.http import HttpResponse
        
        f = StringIO()
        writer = csv.writer(f)
        writer.writerow(["nome", "telefone", "email", "mensagem", "comentario_gelo", "data_envio"])

        for s in queryset:
            writer.writerow([s.nome, s.telefone, s.email, s.mensagem, s.comentario_gelo, s.data_envio])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Planilha_Seguro_Auto.csv'
        return response

    download_csv.short_description = "Baixar planilha(CSV) dos itens selecionados."

class SeguroCasaAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    list_display = ['nome', 'telefone', 'email', 'data_envio']
    list_filter = ['data_envio', 'nome']

    def download_csv(self, request, queryset):
        import csv
        from io import StringIO

        from django.http import HttpResponse
        
        f = StringIO()
        writer = csv.writer(f)
        writer.writerow(["nome", "telefone", "email", "mensagem", "comentario_gelo", "data_envio"])

        for s in queryset:
            writer.writerow([s.nome, s.telefone, s.email, s.mensagem, s.comentario_gelo, s.data_envio])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Planilha_Seguro_Casa.csv'
        return response

    download_csv.short_description = "Baixar planilha(CSV) dos itens selecionados."

class SeguroEmpresaAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    list_display = ['nome', 'telefone', 'email', 'data_envio']
    list_filter = ['data_envio', 'nome']

    def download_csv(self, request, queryset):
        import csv
        from io import StringIO

        from django.http import HttpResponse
        
        f = StringIO()
        writer = csv.writer(f)
        writer.writerow(["nome", "telefone", "email", "mensagem", "comentario_gelo", "data_envio"])

        for s in queryset:
            writer.writerow([s.nome, s.telefone, s.email, s.mensagem, s.comentario_gelo, s.data_envio])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Planilha_Seguro_Empresa.csv'
        return response

    download_csv.short_description = "Baixar planilha(CSV) dos itens selecionados."

class SeguroVidaAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    list_display = ['nome', 'telefone', 'email', 'data_envio']
    list_filter = ['data_envio', 'nome']

    def download_csv(self, request, queryset):
        import csv
        from io import StringIO

        from django.http import HttpResponse
        
        f = StringIO()
        writer = csv.writer(f)
        writer.writerow(["nome", "telefone", "email", "mensagem", "comentario_gelo", "data_envio"])

        for s in queryset:
            writer.writerow([s.nome, s.telefone, s.email, s.mensagem, s.comentario_gelo, s.data_envio])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Planilha_Seguro_Vida.csv'
        return response

    download_csv.short_description = "Baixar planilha(CSV) dos itens selecionados."

class ContatoAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    list_display = ['nome', 'telefone', 'email', 'data_envio']
    list_filter = ['data_envio', 'nome']

    def download_csv(self, request, queryset):
        import csv
        from io import StringIO

        from django.http import HttpResponse
        
        f = StringIO()
        writer = csv.writer(f)
        writer.writerow(["nome", "telefone", "email", "mensagem", "comentario_gelo", "data_envio"])

        for s in queryset:
            writer.writerow([s.nome, s.telefone, s.email, s.mensagem, s.comentario_gelo, s.data_envio])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Planilha_Contato.csv'
        return response

    download_csv.short_description = "Baixar planilha(CSV) dos itens selecionados."



admin.site.register(SeguroViagem, SeguroViagemAdmin)
admin.site.register(SeguroAuto, SeguroAutoAdmin)
admin.site.register(SeguroCasa, SeguroCasaAdmin)
admin.site.register(SeguroEmpresa, SeguroEmpresaAdmin)
admin.site.register(SeguroVida, SeguroVidaAdmin)
admin.site.register(Contato, ContatoAdmin)


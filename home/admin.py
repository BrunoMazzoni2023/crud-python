from django.contrib import admin
from.models import Pessoa, Produto, Venda,Estoque4peca,Estoque1peca

class ListandoPessoa(admin.ModelAdmin):
    list_display = ('id', 'nome','endereco','complemento','cep','telefone','observacao')
    list_display_links = ('nome'),
    list_filter = ('nome',)
    list_per_page = 10
    search_fields = ('nome',)


admin.site.register(Pessoa, ListandoPessoa)
admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(Estoque4peca)
admin.site.register(Estoque1peca)


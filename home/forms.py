from django.forms import ModelForm
from home.models import Pessoa
from home.models import Produto
from home.models import Venda
from home.models import Estoque4peca
from home.models import Estoque1peca
from django.core.exceptions import ValidationError




# Create the form class.

# CLIENTE FORM
class PessoaForm(ModelForm):
    class Meta:
     model = Pessoa
     fields = ['nome','endereco','complemento','cep','telefone','observacao']



# PRODUTO FORM
class ProdutoForm(ModelForm):
     class Meta:
      model = Produto
      fields = ['nome','carro','ano','lado','obs']

# VENDA FORM

class VendaForm(ModelForm):
     class Meta:
      model = Venda
      fields = ['pessoa','produto','placa','carro','valor_peca','obs']

class Estoque4pecaForm(ModelForm):
     class Meta:
      model = Estoque4peca
      fields = ['produto','motorista','passageiro','assento_esquerdo','assento_direito','quantidade_em_estoque', 'estoque_minimo','obs']

class Estoque1pecaForm(ModelForm):
     class Meta:
      model = Estoque1peca
      fields = ['produto','quantidade_em_estoque', 'estoque_minimo', 'obs']


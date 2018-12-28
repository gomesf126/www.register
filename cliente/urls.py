from django.urls import path
#from . import views
from . views import listarCliente
from . views import opcao
from . views import novoCliente
from . views import atualizarCliente
from . views import deletarCliente

urlpatterns = [

	path('novo/', novoCliente, name='novoCliente'),
    path('listar/', listarCliente, name='listarCliente'),
    path('atualizar/<int:id>/', atualizarCliente, name='atualizarCliente'),
    path('deletar/<int:id>/', deletarCliente, name='deletarCliente'),
  	path('opcao/', opcao, name='opcao'),
]

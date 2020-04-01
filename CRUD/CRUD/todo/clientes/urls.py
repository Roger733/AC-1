from django.urls import path
from . import views
urlpatterns = [
    path('helloword/', views.HelloWord),
    path('', views.ClienteList, name='clientes-list'),
    path('cliente/<int:id>',views.clientesView, name="clientes-view"),
    path('novocliente/',views.novoCliente, name="novo-cliente"),
    path('editar/<int:id>',views.editarCliente, name="editar-cliente"),
    path('delete/<int:id>',views.deletarCliente, name="deletar-cliente"),
    

]
from django.urls import path
from django.contrib.auth.views import LogoutView
from Blog.views import *
#inicio,cliente,empleado,pedido, producto, setClientes,getClientes, buscarClientes
#from Pedidos import views
# views.inicio,
# views.cliente,
# etc

urlpatterns = [

    path('', inicio, name='Inicio'),


]
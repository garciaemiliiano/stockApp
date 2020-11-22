from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static #Importar cosas para que muestre archivos staticos
from clientes import views

urlpatterns = [
    path('',views.mostrarTodos, name="clientes"),
    path('add_client/',views.agregarCliente, name="agregar_cliente"),
]
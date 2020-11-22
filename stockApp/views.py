from stockApp.models import Articulos
from django.shortcuts import render, HttpResponse
from stockApp.models import *

def home (request):
    return render (request,"home.html")

def agregar(request):  
    if request.POST ["add"]:
        #mensaje = "Agregado %r" %request.GET["add"]
        """contenido= request.GET ["add"]
        cliente = Cliente.objects.filter(nombre__icontains = contenido)
        return render(request,"resultado.html",{"clientes":cliente,"query":contenido})
        """
        catch = request.GET ["add"]
        clienteNuevo = Cliente.objects.create(nombre = catch)
        return render(request,"resultado.html",{"cliente":clienteNuevo,"query":catch})
    else:
        mensaje = "Debe ingresar un valor"
    
    return HttpResponse(mensaje)



    
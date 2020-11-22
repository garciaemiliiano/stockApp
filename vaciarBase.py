
from stockApp.models import Cliente

def borrarClientes():
    lista = Cliente.objects.all()
    p = lista[0].id
    for i in range (p,len(lista) + p):
        c = Cliente.objects.get (id = i)
        c.delete()


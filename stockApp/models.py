from django.db import models
from django.db.models.base import Model

"""
CLIENTES:
*Cada cliente tiene un NOMBRE, CONTACTO(OP), DOMICILIO(OP), UN PARENTEZCO (OP)

*Tiene una lista de ARTICULOS COMPRADOS, puede tener VARIOS ARTICULOS. 

*Cada ARTICULO, tiene, UN NOMBRE, UNA FECHA DE COMPRA, UN PLAN DE PAGO, UNA LISTA CON FECHAS DE PAGO Y CADA FECHA DE PAGO UN MONTO ESPECIFICO

"""

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    contacto = models.CharField(max_length=10)
    domicilio = models.CharField(max_length=50)
    parentezco = models.CharField(max_length=30)


class Articulos (models.Model):
    nombre = models.CharField(max_length=30)
    fecha = models.DateField(max_length=10)
    plan_de_pago= models.CharField(max_length=10)
    #listaFechaDePago


class Fechas_pago (models.Model):
    fecha = models.DateField()
    pago_finalizado= models.BooleanField()
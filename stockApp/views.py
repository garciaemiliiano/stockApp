from django.shortcuts import render, HttpResponse


"""
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    contacto = models.CharField(max_length=10)
    domicilio = models.CharField(max_length=50)
    parentezco = models.CharField(max_length=30)

"""
def home(request):
    return render(request, "main_templates/home.html")
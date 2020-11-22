
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static #Importar cosas para que muestre archivos staticos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('stockApp.urls','projecto_base'))),
]

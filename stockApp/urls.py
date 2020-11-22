from django.urls import path
from django.contrib import admin
from stockApp import views

urlpatterns = [
    path('',views.home, name="home"),
    path('agregar',views.agregar),
]

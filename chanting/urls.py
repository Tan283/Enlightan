from django.contrib import admin
from django.urls import path
from chanting import views

urlpatterns = [
    path("chanting/<title>/",views.chanting, name="chanting"),
    path("set/<title>/<n>/",views.set,name = "set"),
]
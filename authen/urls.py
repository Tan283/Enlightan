from django.contrib import admin
from django.urls import path
from authen import views


urlpatterns = [
    
    path("signIn/",views.signIn, name='signIn'),
    path("signUp/",views.signUp, name='signUp'),
    path("signOut/",views.signOut, name='singOut'),
    path("deleteAccount/",views.deleteAccount, name='deleteAccount'),
]
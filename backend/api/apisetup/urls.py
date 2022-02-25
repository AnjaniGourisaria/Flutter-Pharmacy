from django.contrib import admin
from django.urls import path, include
from api import views


urlpatterns = [
    path("/update",views.index,name='home')
]

from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [

path('create/',views.create, name='create'),

]

from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('number-print/<int:number>/', views.number_print, name='number_print'),
    path('calculate/<int:number1>/<int:number2>/', views.calculate, name='calculate'),
]
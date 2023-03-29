from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('<int:todo_pk>/', views.detail, name='detail'),
    path('detail/<int:todo_pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
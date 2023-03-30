from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index),
    path('<int:todo_pk>/', views.detail),
    path('index/', views.index, name='index'),
    path('check_completed/<int:todo_pk>/<int:todo_check>', views.check_completed, name='check_completed'),
    path('detail/<int:todo_pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:todo_pk>/delete/', views.delete, name='delete'),
    path('<int:todo_pk>/edit/', views.edit, name='edit'),
    path('<int:todo_pk>/update/', views.update, name='update'),
]
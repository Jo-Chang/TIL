from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index),
    path('<int:pk>/', views.detail, name='detail'),
    
    # new & create Ver-1
    # path('new/', views.new, name='new'),
    # path('create/', views.create, name='create'),
    # new & create Ver-2
    path('new_create/', views.new_create, name='new_create'),
    
    path('<int:pk>/delete/', views.delete, name='delete'),
    
    # edit & update Ver-1
    # path('<int:pk>/edit/', views.edit, name='edit'),
    # path('<int:pk>/update/', views.update, name='update'),
    # edit & update Ver-2
    path('<int:pk>/new_update/', views.new_update, name='new_update'),
]
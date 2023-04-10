from django.urls import path
from . import views


app_name = 'albums'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:album_pk>/delete/', views.delete, name='delete'),
    path('<int:album_pk>/update/', views.update, name='update'),
]

from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:pk>/', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/update/', views.update, name="update"),
    path('category/<int:pk>/', views.category, name="category"),
    path('add_category/', views.add_category, name="add_category"),
]

from django.urls import path
from . import views     # 명시적 상대 경로 => django 권장 form


app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    # path('articles/', views.index),
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    # path('articles/<int:num>/', views.detail),
    path('<int:num>/', views.detail, name='detail'),
    # path('articles/<str:name>/', views.greeting),
    path('hello/<str:name>/', views.greeting, name='greeting'),
]
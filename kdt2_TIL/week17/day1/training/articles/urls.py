from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/comments/', views.comment_create, name='comment_create'),
    path(
        '<int:article_pk>/comments/<int:comment_pk>/delete/',
        views.comment_delete,
        name='comment_delete',
    ),
    path('<int:article_pk>/likes/', views.article_likes, name='article_likes'),
    path('<int:article_pk>/comments/<int:comment_pk>/likes/', views.comment_likes, name='comment_likes'),
    path('<int:article_pk>/emotes/<int:emotion>/', views.emotes, name='emotes'),
]

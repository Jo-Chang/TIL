from . import views
from django.urls import path

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:post_pk>/', views.detail, name='detail'),
    path('<int:post_pk>/answer/<str:answer>', views.answer, name='answer'),
    path('<int:post_pk>/likes/', views.post_like, name='post_like'),
    path('<int:post_pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:post_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
    path('<int:post_pk>/comments/<int:comment_pk>/likes/', views.comment_like, name='comment_like'),
    path('<int:post_pk>/comments/<int:comment_pk>/update/', views.comment_update, name='comment_update'),
]

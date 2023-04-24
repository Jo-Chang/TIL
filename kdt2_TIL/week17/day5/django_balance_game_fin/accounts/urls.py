from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('<int:user_pk>/follows/', views.follows, name='follows'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
]

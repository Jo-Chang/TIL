"""pjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from articles import views  # => url mapping으로 필요 없어짐
# from pages import views   => 이름이 겹침
# from articles import views as articles_view
# from pages import views as pages_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    # path('index/', views.index),
    # path('articles/', views.index),
    # path('dinner/', views.dinner),
    # path('search/', views.search),
    # path('throw/', views.throw),
    # path('catch/', views.catch),
    # path('articles/<int:num>/', views.detail),
    # path('articles/<str:name>/', views.greeting),
    # path('pages/', )
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]
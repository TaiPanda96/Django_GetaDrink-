"""lcbo_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views
from lcbo_app.views import home
from lcbo_app.views import index
from lcbo_app.views import lcbo_promos
from lcbo_app.views import favourites

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lcbo_app/home.html',views.home, name='home'),
    path('lcbo_app/index.html',views.index, name='index'),
    path('lcbo_app/lcbo_promos.html',views.lcbo_promos, name='promos'),
    path('lcbo_app/favourites.html',views.favourites,  name='favourites'),
]

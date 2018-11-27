"""cimetclim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from inicio import views
from servicios import views as views_servicios
from cambioc import views as views_cambioc
from estaciones import views as views_estaciones

urlpatterns = [
    path('servicios/',views_servicios.servicios,name='servicios'),
    path('estaciones/',views_estaciones.Plot2DView.as_view(),name='estaciones'),
    path('cambioc/',views_cambioc.cambioc,name='cambioc'),
    path('', include('inicio.urls')),
    path('admin/', admin.site.urls),
]

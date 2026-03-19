"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path

from myapp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hrc/", views.hrc_detail, name="hrc_detail"),
    path("catalog/", views.catalog, name="catalog"),
    path("ms_sheets/", views.ms_sheets, name="ms_sheets"),
    path("ppgl/", views.ppgl, name="ppgl"),
    path("abrasive_discs/", views.abrasive_discs, name="abrasive_discs"),
    path("welding_wire/", views.welding_wire, name="welding_wire"),
    path('electrodes/', views.electrodes, name='electrodes'),
    path('bolts/', views.bolts, name='bolts'),
    path('grinding/', views.grinding, name='grinding'),
    path('admin/', admin.site.urls),

]



"""cusproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from CUS import views

urlpatterns = [
    # path('', views.homepage),
    path('admin/', admin.site.urls),
    path('/add/cusapp/', views.add_cusapp, name='add_cusapp'),
    path('/edit/cusapp/<int:id>/', views.edit_cusapp, name='edit_cusapp'),
    path('/cusapp/', views.cusapp, name='cusapp'),

]

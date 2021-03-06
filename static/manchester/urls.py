"""manchester URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings

from django.conf.urls import url,include
from django.contrib import admin
from formulario import views
from django.contrib.auth import views as Views

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^$', views.RegistraPaciente,name="RegistraPaciente"),
    url(r'^accounts/login/$', Views.login, name='login'),
    url(r'^accounts/logout/$', Views.logout, name='logout', kwargs={'next_page': '/'}), 
	#url(r'^r$', views.RegistraPaciente,name="formulario"),
]


admin.site.site_header = 'Administração do Manchester'
admin.site.index_title ='Área Administrativa'
admin.site.site_title ='Manchester'


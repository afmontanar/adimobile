from django.conf.urls import url
from django.shortcuts import render_to_response

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^guardar_articulo/$', views.guardar_articulo, name='guardar_articulo'),
]
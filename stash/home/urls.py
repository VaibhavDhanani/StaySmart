from django.urls import path

from home import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
   

]

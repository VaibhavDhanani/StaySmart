from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('home/', views.home, name="home"),
    path('test/', views.my_view),
    path('dashboard',views.dashboard,name='dashboard'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('pg_hostel',views.pg_hostel,name='pg_hostel'),
    path('popup',views.popup,name='popup'),
]

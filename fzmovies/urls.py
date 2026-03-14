from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.fz, name='home'),
    path('series/wonder-man/', views.wonder, name='wonder'),
]
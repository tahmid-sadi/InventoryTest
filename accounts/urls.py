from django.urls import path
from . import views


urlpatterns = [
    path('', views.loginpage, name='login'),
    path('register/', views.register, name='register'),
    path('stocklist/', views.stocklist, name='stocklist'),
    path('logout/', views.logoutuser, name='logout'),
    path('orderspage/', views.orderspage, name='orderspage'),
    path('createpage/', views.createpage, name='createpage'),
    path('productcreatepage/', views.productcreatepage, name='productcreatepage'),
]

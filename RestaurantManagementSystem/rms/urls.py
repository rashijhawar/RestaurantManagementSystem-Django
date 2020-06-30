from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('manager/', views.manager, name='manager'),
    path('chef/', views.chef, name='chef'),
    path('waiter/', views.waiter, name='waiter'),
    path('cashier/', views.cashier, name='cashier'),
    path('menu/', views.item, name='item'),
    path('customer/', views.customer, name='customer'),
    path('bill/', views.bill, name='bill'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customers/add/', views.add_customer, name="add_customer"),
    path('customers/search/', views.search_customer, name='search_customer'),
    path('customers/list/', views.customer_list, name='customer_list'),
]
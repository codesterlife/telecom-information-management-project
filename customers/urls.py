from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_customer, name="add_customer"),
    path('search/', views.search_customer, name='search_customer'),
    path('list/', views.customer_list, name='customer_list'),
]
from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer
from django.db.models import Q
from django.contrib import messages

def home(request):
    return render(request, 'customers/index.html')

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer added successfully!')
            return redirect('customer_list')  # Ensure this matches the name in urls.py
    else:
        form = CustomerForm()
    return render(request, 'customers/add_customer.html', {'form': form})

def search_customer(request):
    query = request.GET.get('q')
    if query:
        customers = Customer.objects.filter(
            Q(customer_name__icontains=query) | Q(customer_id__icontains=query)
        )
        search_performed = True
    else:
        customers = []
        search_performed = False
    return render(request, 'customers/search_customer.html', {'customers': customers, 'search_performed': search_performed})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})

from django.shortcuts import render

from .models import Manager
from .models import Chef
from .models import Waiter
from .models import Cashier
from .models import Item
from .models import Customer
from .models import Bill

def home(request):
    return render(request, 'rms/home.html')

def manager(request):
    manager_list = Manager.objects.all().order_by('managerID')
    return render(request, 'rms/manager.html', {'manager_list': manager_list})

def chef(request):
    chef_list = Chef.objects.all().order_by('chefID')
    return render(request, 'rms/chef.html', {'chef_list': chef_list})

def waiter(request):
    waiter_list = Waiter.objects.all().order_by('waiterID')
    return render(request, 'rms/waiter.html', {'waiter_list': waiter_list})

def cashier(request):
    cashier_list = Cashier.objects.all().order_by('cashierID')
    return render(request, 'rms/cashier.html', {'cashier_list': cashier_list})

def item(request):
    item_list = Item.objects.all().order_by('itemNo')
    return render(request, 'rms/item.html', {'item_list': item_list})

def customer(request):
    customer_list = Customer.objects.all().order_by('customerID')
    return render(request, 'rms/customer.html', {'customer_list': customer_list})

def bill(request):
    bill_list = Bill.objects.all().order_by('billNo')
    return render(request, 'rms/bill.html', {'bill_list': bill_list})
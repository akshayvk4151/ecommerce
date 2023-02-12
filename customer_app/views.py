from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def customer_app_base(request):
    return render(request,'customer_app_templates/base.html')

def customer_app_index(request):
    return render(request,'customer_app_templates/index.html')

def customer_app_product_details(request):
    return render(request,'customer_app_templates/product_details.html')

def customer_app_mycart(request):
    return render(request,'customer_app_templates/mycart.html')


def customer_app_my_order(request):
    return render(request,'customer_app_templates/my_order.html')

def customer_app_change_password(request):
    return render(request,'customer_app_templates/change_password.html')

def customer_app_customer_profile(request):
    return render(request,'customer_app_templates/customer_profile.html')
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def seller_app_seller_home(request):
    return render(request,'seller_app_templates/seller_home.html')
    
def seller_app_homepage(request):
    return render(request,'seller_app_templates/homepage.html')

def seller_app_change_password(request):
    return render(request,'seller_app_templates/change_password.html')

def seller_app_add(request):
    return render(request,'seller_app_templates/add.html')

def seller_app_catalogue(request):
    return render(request,'seller_app_templates/catalogue.html')

def seller_app_update_stock(request):
    return render(request,'seller_app_templates/update_stock.html')

def seller_app_recent_order(request):
    return render(request,'seller_app_templates/recent_order.html')

def seller_app_order_history(request):
    return render(request,'seller_app_templates/order_history.html')

def seller_app_profile(request):
    return render(request,'seller_app_templates/profile.html')
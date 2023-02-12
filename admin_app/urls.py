from django.urls import path
from . import views
app_name='admin_app'

urlpatterns=[
    path('base',views.admin_app_base,name='admin_base'),
    path('admin_home',views.admin_app_admin_home,name='ahome'),
    path('seller_details',views.admin_app_seller_details,name='dseller'),
    path('approve',views.admin_app_approve,name='approve'),
    path('customer_details',views.admin_app_customer_details,name='dcustomer'),


]
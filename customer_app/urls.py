from django.urls import path
from . import views
app_name='customer_app'

urlpatterns=[
    path('base',views.customer_app_base,name='base'),
    path('index',views.customer_app_index,name='home'),
    path('product_details',views.customer_app_product_details,name='pdetails'),
    path('mycart',views.customer_app_mycart,name='mycart'),
    path('my_order',views.customer_app_my_order,name='myorder'),
    
    path('change_password',views.customer_app_change_password,name='password'),
    path('customer_profile',views.customer_app_customer_profile,name='profile'),
]
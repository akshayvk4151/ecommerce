
from django.urls import path
from . import views
app_name='common'

urlpatterns=[
    path('base',views.common_base,name='base'),
    path('index',views.common_index,name='home'),
    path('customer_login',views.common_customer_login,name='customer_login'),
    path('customer_register',views.common_customer_register,name='cus_register'),
    path('seller_register',views.common_seller_register,name='seller_register'),
    path('seller_login',views.common_seller_login,name='seller_login'),
]
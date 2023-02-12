from django.urls import path
from . import views
app_name='seller_app'

urlpatterns=[
    path('seller_home',views.seller_app_seller_home,name='shome'),
    path('homepage',views.seller_app_homepage,name='home'),
    path('change_password',views.seller_app_change_password,name='spassword'),
    path('add',views.seller_app_add,name='add'),
    path('catalogue',views.seller_app_catalogue,name='cat'),
    path('update_stock',views.seller_app_update_stock,name='update_stock'),
    path('recent_order',views.seller_app_recent_order,name='order'),
    path('order_history',views.seller_app_order_history,name='order_history'),
    path('profile',views.seller_app_profile,name='profile'),

]
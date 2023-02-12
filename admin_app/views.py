from django.shortcuts import render
from django.http import HttpResponse
from common.models import Seller
from django.core.mail import send_mail
from random import randint
from django.conf import settings
# Create your views here.



def admin_app_base(request):
    return render(request,'admin_app_templates/base.html')

def admin_app_admin_home(request):
    return render(request,'admin_app_templates/admin_home.html')

def admin_app_seller_details(request):
    sellers = Seller.objects.filter(status = 'approved')
    return render(request,'admin_app_templates/seller_details.html',{'sellers_list':sellers})


def admin_app_approve(request):
    sellers = Seller.objects.filter(status = 'pending')

    if request.method == 'POST':
        seller_id = request.POST['seller_id']
        seller = Seller.objects.get(id = seller_id)

        if 'approve' in request.POST:
            # logic when approve button clicked
           
            
            seller.status = 'approved' #sql update query
            seller.save()
            user_name = randint(1111,9999)
            password = 'sel-' + str(user_name) + str(seller.phone)[5:]
            mail_subject = "Account Approval"
            message_body = "Hi your account has been approved by Admin, You can now login with username" + str(user_name) + " and temprorary password" + password

            
        if 'reject' in request.POST:

            seller.status = 'reject' 
            seller.save()
            
            mail_subject = "Account Rejected"
            message_body = "sorry we cannot approve your request"

        send_mail(
            subject = mail_subject,
            message = message_body,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list= [seller.email]
            )
            


    return render(request,'admin_app_templates/approve.html',{'sellers_list':sellers})

# ///////////////////////////////////////////////////////////////////////////////
def admin_app_customer_details(request):
    return render(request,'admin_app_templates/customer_details.html')
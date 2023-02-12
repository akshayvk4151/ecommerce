from django.shortcuts import render
from django.http import HttpResponse
from.models import Customer, Seller
# Create your views here.

def common_base(request):
    return render(request,'common_templates/base.html')
def common_index(request):
    return render(request,'common_templates/index.html')
def common_customer_login(request):
    return render(request,'common_templates/customer_login.html')
def common_customer_register(request):
    if request.method == 'POST':
        cname = request.POST['customer_name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        gender = request.POST['gender']
        password = request.POST['password']

        customer = Customer(customer_name = cname, email = email, address = address, phone = phone, gender = gender, password = password)
        customer.save()
    return render(request,'common_templates/customer_register.html')


def common_seller_register(request):
    if request.method == 'POST':
        sname = request.POST['seller_name']
        semail = request.POST['email']
        saddress = request.POST['address']
        sphone = request.POST['phone']
        sgender = request.POST['gender']
        scompany_name = request.POST['company_name']
        sholder_name = request.POST['holder_name']
        sifsc = request.POST['ifsc']
        sbranch = request.POST['branch']
        sacc_no = request.POST['account_number']
        simage = request.FILES['image']

        seller = Seller(seller_name = sname, email=semail, address=saddress, phone=sphone, gender=sgender, company_name=scompany_name, holder_name=sholder_name, ifsc=sifsc, branch=sbranch, account_number=sacc_no, image=simage)
        seller.save()
        

    return render(request,'common_templates/seller_register.html')

def common_seller_login(request):
    return render(request,'common_templates/seller_login.html')


from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    gender = models.CharField(max_length=15)
    password = models.CharField(max_length=10,default='')
    status = models.CharField(max_length=20, default='active')



class Seller(models.Model):
    seller_name = models.CharField(max_length=20)
    email = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    user_name = models.IntegerField(default=0)
    password = models.CharField(max_length=40, default='')
    gender = models.CharField(max_length=15)
    company_name = models.CharField(max_length=50)
    holder_name = models.CharField(max_length=20)
    ifsc = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    account_number = models.BigIntegerField()
    image = models.ImageField(upload_to='seller/',default='')
    status = models.CharField(max_length=20, default='pending')

    class Meta:
        db_table = 'seller'

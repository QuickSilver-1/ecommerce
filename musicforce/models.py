from django.db import models


class AdminList(models.Model):
    first_name = models.CharField(max_length=30)   
    last_name = models.CharField(max_length=30)  
    login = models.CharField(max_length=30)       
    password = models.CharField(max_length=30)    

class Customer(models.Model):
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)   
    father_name = models.CharField(max_length=30, blank=True, null=True) 
    age = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)       
    email = models.CharField(max_length=100, blank=True, null=True)      
    adress = models.TextField(blank=True, null=True)
    login = models.CharField(max_length=30)       
    password = models.CharField(max_length=50)    

class Seller(models.Model):
    name = models.CharField(max_length=128)       
    products = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=255)       
    brand = models.CharField(max_length=50)       
    vendor_code = models.IntegerField()
    category = models.CharField(max_length=128)   
    amount_stack = models.IntegerField()
    price = models.IntegerField()  # This field type is a guess.
    discount = models.IntegerField(blank=True, null=True)
    saller = models.ForeignKey(Seller, models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to=f'photos/{category}')

class Bag(models.Model):
    customer = models.OneToOneField(Customer, models.DO_NOTHING)
    product = models.ManyToManyField(Product)
    amount = models.IntegerField()

class Supplie(models.Model):
    saller = models.ForeignKey(Seller, models.DO_NOTHING)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    amount = models.IntegerField()
    delivery_type = models.CharField(max_length=128)
    complited = models.BooleanField(default=False)

class Delivery(models.Model):
    delivery_type = models.CharField(max_length=128)
    price = models.IntegerField()
    status = models.CharField(max_length=128)     

class Transaction(models.Model):
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    product = models.ManyToManyField(Product)
    amount = models.IntegerField()
    purchase_time = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    delivery = models.ForeignKey(Delivery, models.DO_NOTHING, blank=True, null=True)

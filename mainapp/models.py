from django.db import models
from django.contrib.auth.models import AbstractUser 


# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=12)
    address = models.TextField(null= True, blank= True)
    # profile = models.ImageField(null = True,blank = True)
    
    def __str__(self):
        return self.first_name

class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category

class AddProduct(models.Model):
    first_name= models.ForeignKey(User,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=20)
    product_image=models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_price=models.IntegerField(null= False,blank=False)
    description=models.TextField(null= True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    rdate = models.DateField(null=True)
    '''
    def __str__(self):
        return str(self.product_name), str(self.category) , str(self.first_name)
    '''

class AddPrice(models.Model):
    first_name = models.ForeignKey(User,on_delete=models.CASCADE)
    product_name = models.ForeignKey(AddProduct,on_delete=models.CASCADE)
    add_price = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.add_price)

'''


request.user

user==first_name
'''
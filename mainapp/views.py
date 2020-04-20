from django.shortcuts import render , redirect
#from django.contrib.auth.models import User
#from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.http import HttpResponse
from django.contrib.auth import get_user_model
User=get_user_model()
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from . import models
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    if request.method == 'GET':
        # viewproduct=models.AddProduct.objects.values('product_image','product_name','product_price')
        viewproduct=models.AddProduct.objects.all().order_by('-created_at')
        latestbidup = models.AddProduct.objects.all().order_by('rdate') #i.e product by result date
    
        print(latestbidup,'hey success ')
    return render(request,'index.html',{'products':viewproduct,'lb':latestbidup})

def signup_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Sorry !! this email is already exist')
                return redirect(signup_user)
            else:
                messages.info(request,'You are Sign uP Successfully , please lop in now')
                user = User.objects.create_user(username= email, first_name= first_name, last_name=last_name, email = email ,phone =phone, address =  address, password = password1)
                user.save()
                return redirect(index)
        else:
            messages.info(request, 'password not matching')
            return redirect(signup_user)
    else:
        return render(request, 'index.html')


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        user = authenticate(username=email, password=password1)
        print(user)
        if user is not None:
            login(request,user)
            messages.info(request,'successfully login')
            print('successfully login')
            return redirect(index)

        else:
            messages.info(request , 'Invalid Creential')
            return redirect(login_user)
    else:
        return render(request,'index.html')

def logout_user(request):
    logout(request)
    return redirect(index)


def addproduct(request):
    if request.method == 'POST':
        first_name    = request.user
        product_name  = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        description   = request.POST.get('description')
        category   = request.POST.get('category')
        rdate = request.POST.get('rdate') #i.e. result date
        print(category,'catgehgfh')
        cat=models.Category.objects.get(id=category)
        product_image = request.FILES['product_image']
        fs = FileSystemStorage()
        filename = fs.save(product_image.name, product_image)
 
        post = models.AddProduct.objects.create(first_name=first_name, product_name=product_name, product_image=product_image, product_price=product_price, description=description, category=cat,rdate=rdate)
        post.save()
        return redirect(index)
    else:
        cat=models.Category.objects.values('category','id')
        return render(request,'AddProduct.html',{'cat':cat})

def category(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        post = models.Category.objects.create(category= category)
        post.save()
    
    else:
        return render(request, 'addproduct.html')

def viewproduct(request):
    if request.method=='GET':
        viewproduct=models.AddProduct.objects.values('product_image','product_name','product_price')
    return render(request,"index.html",{'products':viewproduct})

def allproduct(request):
    cat=models.Category.objects.values('category','id')
    if request.method=='POST':
        date = request.POST.get("rdate")
        category = request.POST.get('category')
        product_price = request.POST.get('product_price')
        print(date,category,product_price)

        if date =='new' :
            allproduct=models.AddProduct.objects.all().order_by('rdate')
        elif date == 'old':
            allproduct=models.AddProduct.objects.all().order_by('-rdate')
    
        else:
            allproduct=models.AddProduct.objects.all()
        #return render(request,"allproduct.html",{'products':allproduct,'cat':cat})

        if category != "Category":
            category=models.Category.objects.get(id=category)
            allproduct=allproduct.filter(category = category)
            print(allproduct)
        # return render(request,"allproduct.html",{'products':allproduct,'cat':cat})


        if product_price == 'lowest':
            allproduct=allproduct.order_by('product_price')

        elif product_price =="highest":
            allproduct=allproduct.order_by('-product_price')

        return render(request,"allproduct.html",{'products':allproduct,'cat':cat})
          

    else:
        allproduct=models.AddProduct.objects.all()
        # allproduct=models.AddProduct.objects.all().order_by('rdate')
        # allproduct=models.AddProduct.objects.all().order_by('product_price')
        cat=models.Category.objects.values('category','id')
        return render(request,"allproduct.html",{'products':allproduct,'cat':cat})

def productdetails(request,id):
    if request.method=='GET':
        productdetails=models.AddProduct.objects.get(id=id)
        # print(productdetails,'filter output')
        prices = models.AddPrice.objects.filter(product_name=productdetails).last()
        # print(prices,'Lstrdhjgj jkn')
        topten = models.AddPrice.objects.filter(product_name=productdetails).order_by('-add_price')
        print(topten,'top ten bidder')

    return render(request,"productdetails.html",{'products':productdetails,'prices':prices,'topten':topten})

def userprofile(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        print(first_name)
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        profile = request.FILES.get('profile')
        if profile !=None:
            fs = FileSystemStorage()
            filename = fs.save(profile.name, profile)
            request.user.profile=profile.name

        request.user.first_name=first_name
        request.user.last_name=last_name
        request.user.phone=phone
        request.user.address=address
        
        request.user.save()

        return redirect(userprofile)
        
    else:
        form = PasswordChangeForm(request.user)
        return render(request,"userprofile.html",{'users':userprofile,'form':form})

def addprice(request,id):
    if request.method == 'POST':
        first_name    = request.user
        product_name = models.AddProduct.objects.get(id=id)
        #product_price = models.AddProduct.objects.get()
        add_price  = request.POST.get('add_price')
        if int(add_price) > product_name.product_price:
            price = models.AddPrice.objects.create(first_name = first_name ,product_name= product_name , add_price = add_price)
            price.save()
            return redirect (productdetails,id)
        else:
            prices = models.AddPrice.objects.filter(product_name=product_name).last()
            return render(request,"productdetails.html",{'prices':addprice,'products':product_name,'prices':prices})

    else:
        return render(request,"productdetails.html",{'prices':addprice})

def myproduct(request):
    mypros = models.AddProduct.objects.filter(first_name=request.user)
    return render(request,"myproduct.html",{'mypros':mypros})
    
def pdel(request):
    prodel = models.AddProduct.objects.filter(product_name=request.user)
    prodel.delete()
    
    return redirect('myproduct')

            
            

# def topten(request):
#     topten = models.AddPrice.objects.filter()
#     print(topten ,'yeah done')

#     return render(request,"productdetails.html",{'topten':topten})
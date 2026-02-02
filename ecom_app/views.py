from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def product_list(request):
    products=Product.objects.all()
    return render (request,'product_list.html',{'products':products})

def order_list(request):
    orders=order.objects.all()
    return render (request,'order_list.html',{'orders':orders})

def user_list(request):
    users=User.objects.all()
    return render (request,'user_list.html',{'users':users})

def orders_details(request):
    orders1=orderProduct.objects.all()
    return render (request,'orders.html',{'orders1':orders1})

def cart_details(request):
    cart=Cart.objects.all()
    return render (request,'cart1.html',{'cart':cart})

def cart_items(request):
    cartitem=Cart.objects.all()
    return render (request,'cartitem.html',{'cartitem':cartitem})


def firstpage(request):
    return render (request,'fistpage.html')

def Register_user(request):
    if request.method=="POST":
        username=request.POST['username']
        email = request.POST['email'] 
        password = request.POST['password'] 
        confirm_password = request.POST['confirm_password']  
        if password != confirm_password: 
           return render(request, 'register.html', {'error': 'Passwords do not match!'}) 
        if User.objects.filter(username=username).exists(): 
          return render(request, 'register.html', {'error': 'Username already taken!'})
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return redirect(login_user)
    return render(request, 'Register.html') 

@login_required(login_url='login_user')
def dashboard(request):
    return render(request,'product_list.html')

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                # return redirect('/admin/')
                return redirect('product_list')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login_user')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login_user')

# from .models import Product, Cart, CartItem
# from django.shortcuts import get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required

# # @login_required
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     quantity = int(request.POST.get('quantity', 1))

#     cart, created = Cart.objects.get_or_create(user=request.user)

#     # Check if item already exists
#     item, created = CartItem.objects.get_or_create(
#         cart=cart,
#         product=product
#     )

#     if not created:
#         item.quantity += quantity
#     else:
#         item.quantity = quantity

#     item.save()

#     return redirect('view_cart')

# @login_required
# def view_cart(request):
#     cart = request.User.cart
#     items = cart.items.all()
#     return render(request, "cart.html", {"cart": cart, "items": items})

# def delete_item(request, id):
#     item = Cart.objects.get(id=id)
#     item.delete()
#     return redirect('product_list')

# @login_required
# def cart_details(request):
#     cart = Cart.objects.get(user=request.user)
#     cart_items = CartItem.objects.filter(cart=cart)

#     return render(request, 'cart_details.html', {'cart_items': cart_items})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart, created = Cart.objects.get_or_create(user=request.user)
    item, item_created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )
    if not item_created:
        item.quantity += quantity
    else:
        item.quantity = quantity
    item.save()
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    return render(request, "cart.html", {"cart": cart, "items": items})

@login_required
def delete_item(request, id):
    item = get_object_or_404(CartItem, id=id)   # FIXED
    item.delete()
    return redirect('product_list')

@login_required
def cart_items(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cartitem = CartItem.objects.filter(cart=cart)   # FIXED
    return render(request,'cartitem.html', {'cartitem': cartitem})
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
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
        # return redirect(login_user)
    return render(request, 'register.html') 

@login_required(login_url='login_user')
def dashboard(request):
    return render(request,'product_list.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('product_list')
        else:
            messages.error(request, "Invalid username or password!")
            return render(request, 'login.html')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('logout_user')


def session_login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            user=User.objects.get(username=username)

            if user.check_password(password):
                request.session['user_id']=user.id
                request.session['username']=user.username
                request.session['email']=user.email
                return redirect(session_dashboard)
            else:
                return HttpResponse("Invalid password")
        except User.DoesNotExist:
            return HttpResponse("user does not exist")
    return render(request,'login.html')

def session_dashboard(request):
    username_session=request.session.get('username')
    if 'username' in request.session:
        return render(request,'product_list.html',{'username':username_session})
    else:
        return redirect('session_login')
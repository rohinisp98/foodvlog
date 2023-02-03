from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# from shop_app.models import *
# from . models import *
# from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def register(request):

    if request.method=="POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        psw = request.POST['psw']
        psw_repeat = request.POST['pswrepeat']

        if psw == psw_repeat:
            user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=psw)
            user.save()
            messages.success(request, 'registration successfull')
            print("User created")
            return redirect('/')
        else:
            messages.error(request, 'Password does not matching')
            return render(request,'register.html')

    else:
        return render(request,'register.html',{'form':UserCreationForm})

def loginuser(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['psw']
        print(username)
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            print('working here')
            auth.login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('/')
        else:
            messages.error(request, 'Enter valid login details')
            return redirect('loginuser')
    else:
        return render(request,'login.html')
          
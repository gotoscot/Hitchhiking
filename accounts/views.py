from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
# Create your views here.



def login(request):
    return render(request, 'login.html')


def logging(request):
    if request.method=='POST':
        # email = request.POST['email']
        username=request.POST['username']
        pwd = request.POST['password']

        user=auth.authenticate(username=username,password=pwd)
        if user is not None:
            auth.login(request,user)
            messages.info(request, 'accounts successfully!')
            request.session['userid'] = user.id
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
         return render(request,'login.html')


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name=request.POST['last_name']
        email = request.POST['email']
        pwd1=request.POST['password1']
        pwd2 = request.POST['password2']

        if pwd1==pwd2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=pwd1,email=email, first_name=first_name,last_name=last_name)
                user.save();
                print("user created!")
            return redirect('/')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
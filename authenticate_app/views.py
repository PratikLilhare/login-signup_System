from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def loginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=username, password = pwd)
        if user is not None:
            login(request,user)
            return redirect('welcome')
        else:
            messages.error(request,"Username or password is not correct")
            redirect('login')
    return render(request,"login.html")

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request,"User created successfully")
            return redirect('login')
        else:
            messages.error(request,"There was an error")
            
    return render(request,"signup.html",{'form':form})

def home(request):
    user= request.user
    return render(request,'welcome.html',{'user':user})

def logoutPage(request):
    logout(request)
    return redirect ("login")
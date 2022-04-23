from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,"home/login.html")

def sign(request):
    return render(request,"home/signup.html")

def home(request):
    return render(request,"home/home.html")

def master(request):
    return render(request,"home/rent_master.html")

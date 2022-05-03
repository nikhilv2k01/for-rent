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

def properties(request):
    return render(request,"home/display_properties.html")   

def housedetails(request):
    return render(request,"home/house.html") 

def change_pswd(request):
    return render(request,"home/change_pswd.html")

def view_property(request):
    return render(request,"home/view_property.html")

def view_favourites(request):
    return render(request,"home/favourites.html")

def edit_properties(request):
    return render(request,"home/edit_property.html")    

def rent_seller(request):
    return render(request,"home/seller.html")  

def package(request):
    return render(request,"home/package.html")    

def forgot_password(request):
    return render(request,"home/forgot_pswd.html") 

def mstr(request):
    return render(request,"home/master_rent.html")

def viewshop(request):
    return render(request,"home/shops.html")         







    


from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"seller/seller.html")
def shop(request):
    return render(request,"seller/shop.html")  
def pack(request):
    return render(request,"seller/package.html")        
def pay(request):
    return render(request,"seller/pay.html")           
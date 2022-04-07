from django.shortcuts import render

# Create your views here.
def rent(request):
    return render(request,"rent/rent_admin.html")
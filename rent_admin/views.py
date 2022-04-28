from django.shortcuts import render

# Create your views here.
def admin_verify(request):
    return render(request,"rent/rent_admin.html")
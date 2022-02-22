from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,"d.html")
def sign(request):
    return render(request,"e.html")
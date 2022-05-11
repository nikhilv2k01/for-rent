from django.shortcuts import render, redirect
from . models import UserReg


# Create your views here.
def login(request):
    msg = ''
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        user_exist = UserReg.objects.filter(
            user_name=user_name, password=password).exists()
        if user_exist:
            user_data = UserReg.objects.get(
                user_name=user_name, password=password)
            request.session['user_name'] = user_data.user_name
            return redirect("home:main")
        else:
            msg = 'Invalid Username Or Password'


    return render(request, "home/login.html", {'err_msg': msg, })


def sign(request):
    msg=''
    if request.method == 'POST':
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user_exist = UserReg.objects.filter(
            user_name=user_name).exists()
        if user_exist:
            msg="User name already exists"
        else:
            rent_user = UserReg(user_name=user_name, email=email,
                            password=password)
            rent_user.save()

    return render(request, "home/signup.html",{'err_msg':msg,})


def home(request):
    return render(request, "home/home.html")


def master(request):
    return render(request, "home/rent_master.html")


def properties(request):
    return render(request, "home/display_properties.html")


def housedetails(request):
    return render(request, "home/house.html")


def change_pswd(request):
    return render(request, "home/change_pswd.html")


def view_property(request):
    return render(request, "home/view_property.html")


def view_favourites(request):
    return render(request, "home/favourites.html")


def edit_properties(request):
    return render(request, "home/edit_property.html")


def rent_seller(request):
    return render(request, "home/seller.html")


def package(request):
    return render(request, "home/package.html")


def forgot_password(request):
    return render(request, "home/forgot_pswd.html")


def mstr(request):
    return render(request, "home/master_rent.html")


def viewshop(request):
    return render(request, "home/shops.html")


def profile(request):
    return render(request, "home/profile.html")

def logout(request):
    del request.session['user_name']
    request.session.flush()
    return redirect('home:loginnow')

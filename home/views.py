from fileinput import filename
import re

from django.shortcuts import render, redirect
from . models import *
from .decorates import auth_login
import razorpay
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from random import randint, random
from django.core.files.storage import FileSystemStorage
from django.db.models import Q


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
            request.session['user_id'] = user_data.id

            return redirect("home:main")
        else:
            msg = 'Invalid Username Or Password'

    return render(request, "home/login.html", {'err_msg': msg, })


def sign(request):
    msg = ''
    if request.method == 'POST':
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']

        user_exist = UserReg.objects.filter(
            user_name=user_name).exists()
        if user_exist:
            msg = "User name already exists"
        else:
            rent_user = UserReg(user_name=user_name,
                                password=password,  phone=mobile, email=email)
            rent_user.save()

    return render(request, "home/signup.html", {'err_msg': msg, })


@auth_login
def home(request):
    return render(request, "home/home.html")


@auth_login
def master(request):
    return render(request, "home/rent_master.html")


@auth_login
def properties(request, id):
    # if request.method=='POST':
    #     type=request.POST('type')
    #     if type=='houses':
    p_type = ''
    if id == '1':

        p_type = 'House'

    elif id == '2':
        p_type = 'Apartment'
    else:
        p_type = 'Shop'

    properties = PostProperty.objects.filter(type=p_type)

   

    

    return render(request, "home/display_properties.html", {"properties": properties, })


@auth_login
def housedetails(request, id):

    house_details = PostProperty.objects.get(id=id)

   


    return render(request, "home/house.html", {'house_details': house_details, })


@auth_login
def change_pswd(request):
    msg = ''
    details = UserReg.objects.get(user_name=request.session['user_name'])
    password = details.password
    if request.method == "POST":
        current_pass = request.POST['current_pass']
        password1 = request.POST['new_pass']
        confirm_pass = request.POST['confirm_pass']
        if current_pass == password:
            if confirm_pass == password1:
                UserReg.objects.filter(id=details.id).update(
                    password=confirm_pass)
            else:
                msg = 'Password doesnt match'

        else:
            msg = 'current password is invalid'

    return render(request, 'home/change_pswd.html', {'msg': msg, })


@auth_login
def view_property(request):
    view_property=PostProperty.objects.filter(user_id=request.session["user_id"])

    if request.method=='POST':
        delete_id=request.POST["delete_id"]
        property=PostProperty.objects.get(id=delete_id)
        property.delete()
    
    return render(request, "home/view_property.html",{"view":view_property,})


def delete_property(request,id):
    PostProperty.objects.get(id=id).delete()
    return redirect("home:viewproperty")



@auth_login
def view_favourites(request):
    view_favourites=Favourites.objects.filter(login_id=request.session["user_id"])
    
    return render(request, "home/favourites.html",{"view_favourites":view_favourites,})


@auth_login
def edit_properties(request,id):
    edit_property=PostProperty.objects.get(id=id)

    return render(request, "home/edit_property.html",{"edit":edit_property,})


@auth_login
def rent_seller(request):
    if request.method == 'POST':

        type = request.POST['type']
        owner_name = request.POST['owner_name']
        bed = request.POST['bed']
        bath = request.POST['bath']
        furnishing = request.POST['furnishing']
        built_area = request.POST['built']
        carpet_area = request.POST['carpet']
        total_floor = request.POST['tfloor']
        floor_no = request.POST['floor_no']
        bachelors_allowed = request.POST['bachelor']
        street = request.POST['street']
        district = request.POST['district']
        upload_images = request.FILES['upload_img']

        price = request.POST['price']
        contact_no = request.POST['contact_no']
        img = str(upload_images)

        file_name = str(randint(11111, 99999))+upload_images.name
        print(file_name)

        fileObj = FileSystemStorage()
        fileObj.save(file_name, upload_images)

        if type == 'Shop':

            request.session['data1'] = [type, owner_name, furnishing, built_area, carpet_area,
                                        total_floor, floor_no, street, district, file_name, price, contact_no ]
        else:

            request.session['data2'] = [type, owner_name, bed, bath, furnishing, built_area, carpet_area,
                                        total_floor, floor_no, bachelors_allowed, street, district, file_name, price, contact_no, ]

        return redirect('home:pkgs')
    return render(request, "home/seller.html")


@auth_login
def package(request):
    # data=request.session['data2']
    # userId = request.session['user_id']
    # usr = UserReg.objects.get(id=userId)


    return render(request, "home/package.html")


def selectbasic(request):
    userId = request.session['user_id']
    usr = UserReg.objects.get(id=userId)
    if 'data2' in request.session:

        data = request.session['data2']

        property = PostProperty(type=data[0], owner_name=data[1], bed=data[2], bath=data[3],
                                furnishing=data[4], built_area=data[5], carpet_area=data[6], total_floor=data[7],
                                floor_no=data[8], bachelors_allowed=data[9], street=data[10], district=data[11], upload_images=data[12],
                                price=data[13], contact_no=data[14], user_id=usr,status=False)
        property.save()
        del request.session['data2']
        return redirect("home:main")

    else:
        data = request.session['data1']
        property = PostProperty(type=data[0], owner_name=data[1], bed='0', bath='0',
                                furnishing=data[2], built_area=data[3], carpet_area=data[4], total_floor=data[5],
                                floor_no=data[6], bachelors_allowed='', street=data[7], district=data[8], upload_images=data[9],
                                price=data[10], contact_no=data[11], user_id=usr,status=False)
        
        property.save()
        del request.session['data1']

    return render(request, "home/home.html")


def selectPremium(request):
    userId = request.session['user_id']
    usr = UserReg.objects.get(id=userId)
    if 'data2' in request.session:

        data = request.session['data2']

        property = PostProperty(type=data[0], owner_name=data[1], bed=data[2], bath=data[3],
                                furnishing=data[4], built_area=data[5], carpet_area=data[6], total_floor=data[7],
                                floor_no=data[8], bachelors_allowed=data[9], street=data[10], district=data[11], upload_images=data[12],
                                price=data[13], contact_no=data[14], user_id=usr,status=True)
        
        property.save()
        del request.session['data2']
        return redirect("home:main")

    else:
        data = request.session['data1']
        property = PostProperty(type=data[0], owner_name=data[1], bed='0', bath='0',
                                furnishing=data[2], built_area=data[3], carpet_area=data[4], total_floor=data[5],
                                floor_no=data[6], bachelors_allowed='', street=data[7], district=data[8], upload_images=data[9],
                                price=data[10], contact_no=data[11], user_id=usr,status=True)
        property.save()
        del request.session['data1']
        

    return render(request, "home/home.html")


@auth_login
def forgot_password(request):
    return render(request, "home/forgot_pswd.html")


@auth_login
def mstr(request):
    return render(request, "home/master_rent.html")


@auth_login
def viewshop(request,id):

    shop_details = PostProperty.objects.get(id=id)

    return render(request, "home/shops.html",{"shop_details":shop_details,})


@auth_login
def profile(request):
    userId = request.session['user_id']
    profile = UserReg.objects.get(id=userId)
    if request.method == 'POST':
        image = request.FILES['photo']
        fname = request.POST['fname']
        lname = request.POST['lname']
        dateofbirth = request.POST['dateofbirth']
        phone = request.POST['phone']
        email = request.POST['email']
        city = request.POST['city']
        state = request.POST['state']
        UserReg.objects.filter(id=userId).update(upload_image=image, first_name=fname, last_name=lname,
                                         dateofbirth=dateofbirth, phone=phone, email=email, city=city, state=state)
        return redirect("home:main")

    return render(request, "home/profile.html", {"profile": profile, })


def logout(request):
    del request.session['user_name']
    request.session.flush()
    return redirect('home:loginnow')


@csrf_exempt
def packageselect(request):
    order_amount = request.POST['totalprice']
    order_currency = 'INR'
    type(order_amount)
    client = razorpay.Client(
        auth=('rzp_test_jSJtKTJ5JPeABv', 'bKYuB0sQmjXqQpk1WHtktMkj'))
    payment = client.order.create(
        {"amount": order_amount, "currency": order_currency})
    return JsonResponse(payment)


@csrf_exempt
def packageselectpremium(request):
    order_amount = request.POST['totalprice']
    order_currency = 'INR'
    type(order_amount)
    client = razorpay.Client(
        auth=('rzp_test_jSJtKTJ5JPeABv', 'bKYuB0sQmjXqQpk1WHtktMkj'))
    payment = client.order.create(
        {"amount": order_amount, "currency": order_currency})
    
    return JsonResponse(payment)

def search(request):
    
    if request.method == 'GET':
        user_name = request.GET.get('search')
        status = PostProperty.objects.filter(Q(district__icontains=user_name) | Q(street__icontains=user_name)| Q(price__icontains=user_name))
        
        return render(request, "home/search.html", {"username": status, })

    return render(request,"home/search.html")


def favourites(request,id):
    property=PostProperty.objects.get(id=id)
    user=UserReg.objects.get(id=request.session["user_id"])

    already_exist = Favourites.objects.filter(
        login_id=request.session['user_id'], property_id=id).exists()
    if not already_exist:
        
        fav = Favourites(login_id=user, property_id=property)
        fav.save()

        return redirect("home:viewfavourites")
    else:
        return redirect("home:main")



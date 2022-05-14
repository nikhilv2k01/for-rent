from django.shortcuts import render, redirect
from . models import UserReg, PostProperty
from .decorates import auth_login
import razorpay
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt



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
    msg = ''
    if request.method == 'POST':
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user_exist = UserReg.objects.filter(
            user_name=user_name).exists()
        if user_exist:
            msg = "User name already exists"
        else:
            rent_user = UserReg(user_name=user_name, email=email,
                                password=password)
            rent_user.save()

    return render(request, "home/signup.html", {'err_msg': msg, })


@auth_login
def home(request):
    return render(request, "home/home.html")


@auth_login
def master(request):
    return render(request, "home/rent_master.html")


@auth_login
def properties(request):
    return render(request, "home/display_properties.html")


@auth_login
def housedetails(request):

    return render(request, "home/house.html")


@auth_login
def change_pswd(request):
    msg=''
    details=UserReg.objects.get(user_name=request.session['user_name'])
    password=details.password
    if request.method=="POST":
        current_pass=request.POST['current_pass']
        password1=request.POST['new_pass']
        confirm_pass=request.POST['confirm_pass']
        if current_pass==password:
            if confirm_pass==password1:
                UserReg.objects.get(id=details.id).update(password=confirm_pass)
            else:
                msg='Password doesnt match'

        else:
            msg='current password is invalid'

    return render(request, 'home/change_pswd.html',{'msg':msg,}) 
   


@auth_login
def view_property(request):
    return render(request, "home/view_property.html")


@auth_login
def view_favourites(request):
    return render(request, "home/favourites.html")


@auth_login
def edit_properties(request):
    return render(request, "home/edit_property.html")


@auth_login
def rent_seller(request):
    if request.method == 'POST':
        type = request.POST['type']
        owner_name = request.POST['ower_name']
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
        if type == 'shops':
            
            property = PostProperty(type=type, owner_name=owner_name, bed='0', bath='0',
                                    furnishing=furnishing, built_area=built_area, carpet_area=carpet_area, total_floor=total_floor,
                                    floor_no=floor_no, bachelors_allowed='none', street=street, district=district, upload_images=upload_images,
                                    price=price, contact_no=contact_no)
            # property.save()
            request.session['data1'] = [type, owner_name, furnishing, built_area, carpet_area,
                                       total_floor, floor_no, street, district, upload_images, price, contact_no]
        else:
            property = PostProperty(type=type, owner_name=owner_name, bed=bed, bath=bath,
                                    furnishing=furnishing, built_area=built_area, carpet_area=carpet_area, total_floor=total_floor,
                                    floor_no=floor_no, bachelors_allowed=bachelors_allowed, street=street, district=district, upload_images=upload_images,
                                    price=price, contact_no=contact_no)

            request.session['data2'] = [type, owner_name, furnishing,bed,bath, built_area, carpet_area,
                                       total_floor, floor_no,bachelors_allowed, street, district, upload_images, price, contact_no]                        



            # property.save()
    return render(request, "home/seller.html")


@auth_login
def package(request):
    pack = request.POST['package']
    data1=request.session['data1']
    type=data1[1]
    owner_name=data1[2]
    furnishing=data1[3]
    built_area=data1[4]
    carpet_area=data1[5]
    total_floor=data1[6]
    floor_no=data1[7]
    street=data1[8]
    district=data1[9]
    upload_images=data1[10]
    price=data1[11]
    contact_no=data1[12]


    data2=request.session['data2']
    type=data2[1]
    owner_name=data2[2]
    furnishing=data2[3]
    bed=data2[4]
    bath=data2[5]
    built_area=data2[6]
    carpet_area=data2[7]
    total_floor=data2[8]
    floor_no=data2[9]
    bachelors_allowed=data2[10]
    street=data2[11]
    district=data2[12]
    upload_images=data2[13]
    price=data2[14]
    contact_no=data2[15]
    if data1 != "":
         property = PostProperty(type=type, owner_name=owner_name, bed='0', bath='0',
                                    furnishing=furnishing, built_area=built_area, carpet_area=carpet_area, total_floor=total_floor,
                                    floor_no=floor_no, bachelors_allowed='none', street=street, district=district, upload_images=upload_images,
                                    price=price, contact_no=contact_no)
         property.save()
    if data2!="":
        property = PostProperty(type=type, owner_name=owner_name, bed=bed, bath=bath,
                                    furnishing=furnishing, built_area=built_area, carpet_area=carpet_area, total_floor=total_floor,
                                    floor_no=floor_no, bachelors_allowed=bachelors_allowed, street=street, district=district, upload_images=upload_images,
                                    price=price, contact_no=contact_no)

        property.save()

    return render(request, "home/package.html")


@auth_login
def forgot_password(request):
    return render(request, "home/forgot_pswd.html")


@auth_login
def mstr(request):
    return render(request, "home/master_rent.html")


@auth_login
def viewshop(request):
    return render(request, "home/shops.html")


@auth_login
def profile(request):
    return render(request, "home/profile.html")


def logout(request):
    del request.session['user_name']
    request.session.flush()
    return redirect('home:loginnow')


@csrf_exempt
def packageselect(request):
    order_amount = request.POST['totalprice']
    order_currency = 'INR'
    type(order_amount)
    client = razorpay.Client(auth=('rzp_test_jSJtKTJ5JPeABv','bKYuB0sQmjXqQpk1WHtktMkj'))
    payment = client.order.create({"amount": order_amount, "currency": order_currency})
    return JsonResponse(payment)

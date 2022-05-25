from fileinput import filename
 
from django.shortcuts import render, redirect
from . models import UserReg, PostProperty
from .decorates import auth_login
import razorpay
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from random import randint, random
from django.core.files.storage import FileSystemStorage


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
def properties(request,id):
    # if request.method=='POST':
    #     type=request.POST('type')
    #     if type=='houses':
    p_type=''
    if id=='1':

            p_type='houses'
           
    elif id=='2':
        p_type='apartments'
    else:
        p_type='shops'

    properties=PostProperty.objects.filter(type=p_type)
    return render(request, "home/display_properties.html",{"properties":properties,})


@auth_login
def housedetails(request ,id):
    

    house_details=PostProperty.objects.get(id=id)

    return render(request, "home/house.html",{'house_details':house_details,})


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
        img=str(upload_images)
        
        file_name=str(randint(11111,99999))+upload_images.name
        print(file_name)
        
        fileObj=FileSystemStorage()
        fileObj.save(file_name, upload_images)


        if type == 'shops':
            
            request.session['data1'] = [type, owner_name, furnishing, built_area, carpet_area,
                                       total_floor, floor_no, street, district, file_name, price, contact_no,]
        else:

           
            request.session['data2'] = [type, owner_name,bed ,bath,furnishing, built_area, carpet_area,
                                       total_floor, floor_no,bachelors_allowed, street, district, file_name, price, contact_no,]                        



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
       
        data=request.session['data2']
        
    
        property = PostProperty(type=data[0], owner_name=data[1], bed=data[2], bath=data[3],
                                furnishing=data[4], built_area=data[5], carpet_area=data[6], total_floor=data[7],
                                floor_no=data[8], bachelors_allowed=data[9], street=data[10], district=data[11], upload_images=data[12],
                                price=data[13], contact_no=data[14], user_id=usr)
        property.save()   
        del request.session['data2']
        
                             
    else:
        data=request.session['data1']
        property = PostProperty(type=data[0], owner_name=data[1], bed='0', bath='0',
                                    furnishing=data[2], built_area=data[3], carpet_area=data[4], total_floor=data[5],
                                    floor_no=data[6], bachelors_allowed='', street=data[7], district=data[8], upload_images=data[9],
                                    price=data[10], contact_no=data[11],user_id=usr)
        property.save() 
        del request.session['data1'] 
    

    return render(request,"home/package.html")



def selectPremium(request):
    userId = request.session['user_id']
    usr = UserReg.objects.get(id=userId)
    if 'data2' in request.session:
       
        data=request.session['data2']
        
    
        property = PostProperty(type=data[0], owner_name=data[1], bed=data[2], bath=data[3],
                                furnishing=data[4], built_area=data[5], carpet_area=data[6], total_floor=data[7],
                                floor_no=data[8], bachelors_allowed=data[9], street=data[10], district=data[11], upload_images=data[12],
                                price=data[13], contact_no=data[14], user_id=usr)
        property.save()   
        del request.session['data2']
        
                             
    else:
        data=request.session['data1']
        property = PostProperty(type=data[0], owner_name=data[1], bed='0', bath='0',
                                    furnishing=data[2], built_area=data[3], carpet_area=data[4], total_floor=data[5],
                                    floor_no=data[6], bachelors_allowed='', street=data[7], district=data[8], upload_images=data[9],
                                    price=data[10], contact_no=data[11],user_id=usr)
        property.save() 
        del request.session['data1'] 
    

    return render(request,"home/package.html")





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


@csrf_exempt
def packageselectpremium(request):
    order_amount = request.POST['totalprice']
    order_currency = 'INR'
    type(order_amount)
    client = razorpay.Client(auth=('rzp_test_jSJtKTJ5JPeABv','bKYuB0sQmjXqQpk1WHtktMkj'))
    payment = client.order.create({"amount": order_amount, "currency": order_currency})
    return JsonResponse(payment)


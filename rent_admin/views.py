from msilib.schema import Property
from django.shortcuts import render,redirect
from . models import AdminLog
from .decorates import auth_login
from home.models import PostProperty, UserReg

# Create your views here.
@auth_login
def admin_verify(request):
    
    admin_verify=PostProperty.objects.filter(status=True, premium_package = False)               
    return render(request,"rent/rent_admin.html",{"verify":admin_verify})

def premium_verify(request,id):
    PostProperty.objects.filter(id=id).update(premium_package=True)
    return redirect('rent_admin:verify')

def admin_log(request):
    msg=''
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user_exist=AdminLog.objects.filter(user_name=username,password=password).exists()
        if user_exist:
            user_data=AdminLog.objects.get(user_name=username,password=password)
            request.session['adm_id']=user_data.id
            return redirect("rent_admin:verify")
        else:
            msg="Invalid Username Or Password"    

    return render(request,"rent/admin_login.html",{'err_msg':msg,})

@auth_login
def logout(request):
    del request.session['adm_id']
    request.session.flush()
    return redirect('rent_admin:login')

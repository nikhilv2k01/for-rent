from django.shortcuts import render,redirect
from . models import AdminLog

# Create your views here.
def admin_verify(request):
    return render(request,"rent/rent_admin.html")

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


def logout(request):
    del request.session['adm_id']
    request.session.flush()
    return redirect('rent_admin:login')

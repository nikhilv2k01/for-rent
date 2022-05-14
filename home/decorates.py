from django.shortcuts import render,redirect
def auth_login(func):
    def wrap(request,*args,**kwargs):
        if 'user_name' in request.session:
            return func(request,*args,**kwargs)
        else:
            return redirect('home:loginnow')
    return wrap
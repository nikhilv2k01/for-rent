from unicodedata import name
from . import views
from django.urls import path
app_name = 'home'
urlpatterns = [
    path('', views.login, name="loginnow"),
    path('sign', views.sign, name="submit"),
    path('home', views.home,name="main"),
    path('master', views.master),
    path('display', views.properties,name="display"),
    path('house', views.housedetails,name="details"),
    path('password', views.change_pswd,name="change"),
    path('property', views.view_property,name="viewproperty"),
    path('favourites', views.view_favourites,name="viewfavourites"),
    path('edit', views.edit_properties,name="user_edit"),
    path('seller',views.rent_seller,name="rentseller"),
    path('pack',views.package,name="pkgs"),
    path('forgot',views.forgot_password,name="pforgot"),
    path('mas',views.mstr),
    path('shops',views.viewshop),
    path('profile',views.profile,name="myprofile"),
    path('logout',views.logout,name="out")
    
 
]

from unicodedata import name
from . import views
from django.urls import path
app_name = 'home'
urlpatterns = [
    path('', views.login, name="loginnow"),
    path('sign', views.sign, name="submit"),
    path('home', views.home,name="main"),
    path('master', views.master),
    path('display/<str:id>', views.properties,name="display"),
    path('house/<int:id>', views.housedetails,name="house"),
    path('password', views.change_pswd,name="change"),
    path('property', views.view_property,name="viewproperty"),
    path('favourites', views.view_favourites,name="viewfavourites"),
    path('edit/<int:id>', views.edit_properties,name="user_edit"),
    path('seller',views.rent_seller,name="rentseller"),
    path('pack',views.package,name="pkgs"),
    path('forgot',views.forgot_password,name="pforgot"),
    path('mas',views.mstr),
    path('shops/<int:id>',views.viewshop ,name="shop"),
    path('profile',views.profile,name="myprofile"),
    path('logout',views.logout,name="out"),
    path('packageselect',views.packageselect,name="packageselect"),
    path('selectbasic',views.selectbasic,name="selectbasic"),
    path('packageselectpremium',views.packageselectpremium,name="packageselectpremium"),

    path('selectPremium',views.selectPremium,name="selectPremium"),
    path('search',views.search,name="search"),
    path('favourites/<int:id>',views.favourites,name="favourites"),

    path('delete_property/<int:id>',views.delete_property,name="delete_property"),

    
 
]

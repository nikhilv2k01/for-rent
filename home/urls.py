from . import views
from django.urls import path
app_name = 'home'
urlpatterns = [
    path('', views.login, name="loginnow"),
    path('sign', views.sign, name="submit"),
    path('home', views.home),
    path('master', views.master)
 
]

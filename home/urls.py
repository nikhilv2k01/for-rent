from . import views
from django.urls import path
urlpatterns=[
    path('',views.login),
    path('sign',views.sign , name="sin"),
    path('home',views.home)
]
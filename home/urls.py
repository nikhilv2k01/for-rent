from . import views
from django.urls import path
urlpatterns=[
    path('',views.Home),
    path('sg',views.sign , name="sin"),
    path('hm',views.hom)
]
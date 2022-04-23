from . import views
from django.urls import path
app_name='buyer'
urlpatterns=[
    path('app3',views.Home)
]

from . import views
from django.urls import path
app_name='rent_admin'
urlpatterns=[
    path('verify',views.admin_verify,name="verify"),
    path('admlogin',views.admin_log,name="login"),
    path('logout',views.logout,name="out"),
    path('premium/<int:id>',views.premium_verify,name="premium"),

]

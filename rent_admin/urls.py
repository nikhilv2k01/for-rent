from . import views
from django.urls import path
app_name='rent_admin'
urlpatterns=[
    path('verify',views.admin_verify),
]

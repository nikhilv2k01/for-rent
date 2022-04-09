from . import views
from django.urls import path
urlpatterns=[
    path('house',views.home),
    path('shop',views.shop,name="sh"),
    path('pack',views.pack),
    path('pay',views.pay)
]
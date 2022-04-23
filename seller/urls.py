from . import views
from django.urls import path
app_name='seller'
urlpatterns=[
    path('house',views.home,name="house"),
    path('shop',views.shop,name="sh"),
    path('pack',views.pack),
    path('pay',views.pay)
]
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', "ecommerce.views.ecommerce_home",name="home"),
    url(r'^register/$', "ecommerce.views.register",name="register"),
    url(r'^login/$', "ecommerce.views.user_login", name="login"),
    url(r'^logout/$', "ecommerce.views.user_logout",name="logout"),
    url(r'^myorders/$', "ecommerce.views.user_order",name="order"),
    url(r'^products/$', "ecommerce.views.product_detail",name="p_detail"),
]
# name='register'
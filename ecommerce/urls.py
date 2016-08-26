from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', "ecommerce.views.ecommerce_home"),
    url(r'^register/$', "ecommerce.views.register",name="register"),
    url(r'^login/$', "ecommerce.views.user_login", name="login"),
    url(r'^logout/$', "ecommerce.views.user_logout",name="logout"),
]
# name='register'
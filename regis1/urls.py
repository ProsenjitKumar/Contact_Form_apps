from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'home/$', views.Home, name='home'),
    url(r'reg/$', views.Reg, name='reg'),
]
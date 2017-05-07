from django.conf.urls import url 
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
	url(r'^$', views.signup , name = 'start'),
	url(r'^signup/$', views.signup , name = 'signup' ),
	url(r'^login/$', auth_views.login, {'template_name': 'index2.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^accounts/profile/', views.home , name = 'home' ),
    url(r'^performances/',views.performances,name = 'performances'),
    url(r'^video/',views.video,name='video'),
    url(r'^stream/',views.stream,name='stream'),
    url(r'^stream2/',views.stream2,name='stream2')

]
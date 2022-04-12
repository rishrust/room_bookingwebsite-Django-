from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signinmanager/',views.signinmanager,name='signinmanager'),
    path('logout_view/',views.logout_view,name='logout')
]

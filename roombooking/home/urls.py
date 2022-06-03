from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('logout_view/',views.logout_view,name='logout'),
    path('signinmanager/',include('room.urls')),
    path('bookroom/',include('bookroomuser.urls')),
]

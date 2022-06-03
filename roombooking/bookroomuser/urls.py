from django.urls import path
from . import views

urlpatterns = [ path('',views.bookroom,name='bookroom'),
path('viewbooking/',views.viewbooking,name='view booking')
]

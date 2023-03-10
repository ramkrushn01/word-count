from django.urls import path
from adminpanel import views

urlpatterns = [
    path('',views.index,name='index'),
    path('loginU',views.loginUser,name='login'),
    path('logoutU',views.logoutUser,name='logout'),
]
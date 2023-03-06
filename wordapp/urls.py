from django.urls import path
from wordapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('membership',views.membership,name='membership'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('login',views.loginUser,name='login'),
    path('logout',views.logoutUser,name='logout'),
    path('signup',views.signUpUser,name='signup'),
    path('history',views.textHistory,name='history'),
    path('savefile',views.saveFile,name='savefile'),
    path('forgotpassword',views.forgotPassword,name='forgotpassword'),
]

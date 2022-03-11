from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('registerpage/', views.register_page, name= "register-page"),
    path('loginpage/', views.login_page, name = "login-page"),
    path('logout/', views.logout_my, name = "logout-user"),
    path('login/', views.login_my , name="authenticate-user"),
    path('profile/', views.profile_page , name="profile-page"),    
]

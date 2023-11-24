from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('contact/', views.contact, name="contact"),
    path('enroll/', views.enroll_now, name="enroll"),
    path('profile/', views.profile, name="profile"),
]

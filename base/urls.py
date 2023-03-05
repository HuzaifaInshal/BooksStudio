from django.urls import path
from . import views

urlpatterns=[
    path('',views.splash,name="splash"),
    path('land/',views.land,name="land"),
    path('login/',views.account,name="account"),
    path('main/<str:pk>/',views.main,name="main"),
    path('test',views.test,name="test"),
    path('logout/',views.logoutUser, name="logout"),


]
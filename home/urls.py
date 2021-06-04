
from django.urls import path
from django.shortcuts import render, HttpResponse
from home import views

urlpatterns = [
   path("",views.index, name="home"),
   path("about",views.about,name="about"),
   path("contactus",views.contactus,name="contactus"),
   path("physics",views.physics,name="physics"),
   path("chemistry",views.chemistry,name="chemistry"),
   path("maths",views.maths,name="maths"), 
   path("biology",views.biology,name="biology"),
]
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns=[

    path("home", views.home , name = 'home'),
    path('',  views.home ,name='home'),
    path("adduser", views.adduser, name ='adduser'),
    path("removeuser/<int:id>", views.removeuser, name ="removeuser"),
    path("listspeakers", views.listspeakers, name ='listspeakers')
    
]
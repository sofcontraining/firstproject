from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about',views.about),
    path('courses',views.courses),
    path('<str:slug>',views.coursedetails),
    path('contact',views.contact),
    path('portfolio',views.portfolio),
]
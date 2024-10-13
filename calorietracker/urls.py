"""
URL configuration for calorietracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tracker import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('signup/', views.signup, name='signup'),  
    path('login/', views.login_view, name='login'), 
    path('logout/', views.logout, name='logout'),  
    path('dashboard/', views.dashboard, name='dashboard'),  
    path('add_food/', views.add_food, name='add_food'),  
    path('remove_food/<int:food_id>/', views.remove_food, name='remove_food'),
    path('reset_calories/', views.reset_calories, name= 'reset_calories')
]

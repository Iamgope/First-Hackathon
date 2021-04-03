from os import name
from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('dashboard/', views.Dashboard, name='dashboard'),
]

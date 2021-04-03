from os import name
from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/',views.upload,name= 'upload'),
    path('item_des/',views.item_desc,name= 'description'),

]

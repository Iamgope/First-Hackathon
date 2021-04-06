from os import name
from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('',views.home, name = 'home'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('upload/',views.upload, name = 'upload'),
    path('categories/', views.category, name = 'category'),
    path('items/<int:pk>/',views.itemDetails,name="details"),
    path('categories/books',views.books, name = 'books'),
    path('categories/clothes',views.clothes, name = 'clothes'),
    path('categories/bike',views.bike, name = 'bike'),
    path('categories/music',views.music, name = 'music'),




]

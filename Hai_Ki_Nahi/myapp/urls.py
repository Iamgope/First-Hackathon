from os import name
from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('',views.home, name = 'home'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('upload/',views.upload, name = 'upload'),
    path('categories/', views.category, name = 'category'),
    path('item_des/<int:item_id>/',views.item_desc, name = 'description'),
    path('categories/books',views.books, name = 'books'),
    path('categories/clothes',views.clothes, name = 'clothes'),
    path('categories/bike',views.bike, name = 'bike'),
    path('categories/music',views.music, name = 'music'),




]

from django.shortcuts import redirect, render
from myapp.forms import ItemForm
from django.contrib import messages
from .models import *
# Create your views here.

def home(request):
    return render(request,'home.html')
    
def dashboard(request):
    return render(request,'dashboard.html')

def upload(request):
    if request.method == 'POST':
        form = ItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp:home')
        else:
            return redirect('myapp:dashboard')
    else:
        form = ItemForm()
        return render(request,'upload.html',{'form':form})

def category(request):
    return render(request,'categories.html')

def item_desc(request):
    return render(request,'item_description.html')

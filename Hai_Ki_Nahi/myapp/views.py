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
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'item_description.html', { 'item': item })
    # else:
    #     return redirect('myapp:dashboard')

def books(request):
    items=Item.objects.filter(Tag="choice1")
    return render(request,'item_list.html',{'type':'Books','items':items})


def music(request):
    items=Item.objects.filter(Tag="choice2")
    return render(request,'item_list.html',{'type':"Instruments",'items':items})


def clothes(request):
    items=Item.objects.filter(Tag="choice4")
    return render(request,'item_list.html',{'type':"Clothes",'items':items})


def bike(request):
    items=Item.objects.filter(Tag="choice3")
    return render(request,'item_list.html',{'type':"Bike",'items':items})



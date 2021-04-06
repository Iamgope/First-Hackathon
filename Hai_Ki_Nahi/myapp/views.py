from django.shortcuts import redirect,get_object_or_404,render
from myapp.forms import ItemForm
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def home(request):
    return render(request,'home.html')
    
def dashboard(request):
    return render(request,'dashboard.html')

@login_required
def upload(request):
    
    if request.method == 'POST':
        form = ItemForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            it=form.save(commit=False)
            it.username=request.user
            it.save()

            return redirect('myapp:home')
        else:
            print("somtihng wrong")
            return redirect('myapp:dashboard')
    else:
        form = ItemForm()
        return render(request,'upload.html',{'form':form})

def category(request):
    return render(request,'categories.html')

def item_desc(request, item_id):
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

def itemDetails(request,pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        if item.Available:
            item.Available=False
            item.save()
            return redirect('myapp:dashboard')
        else:
            return render(request,'item_description.html',{'item':item})
    else:
        return render(request,'item_description.html',{'item':item})


from django.shortcuts import redirect, render
from myapp.forms import ItemForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')
    
def Dashboard(request):
    return render(request,'dashboard.html')


def upload(request):
    uploaded  = False
    if request.method == 'POST':
        itemform = ItemForm(request.POST)
        if itemform.is_valid():
            itemform.save(commit=True)
            uploaded = True
            messages.info(request,"you have uploaded your belongings successfully !!")
            return redirect('home')



    return render(request,'upload.html',{'itemform':ItemForm,'uploaded':uploaded})
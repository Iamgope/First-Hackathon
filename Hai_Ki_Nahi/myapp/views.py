from django.shortcuts import redirect, render
from myapp.forms import ItemForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')
    
def Dashboard(request):
    return render(request,'dashboard.html')


def upload(request):
    if request.method == 'POST':
        itemform = ItemForm(request.POST)
        if itemform.is_valid():
            itemform.save(commit=True)
            return redirect('home')
        else:
            print('some error')


    return render(request,'upload.html',{'itemform':ItemForm})
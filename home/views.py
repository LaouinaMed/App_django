from django.shortcuts import render
from django.http import HttpResponse
from listing.models import Placement
from multiprocessing import context
from django.shortcuts import redirect, render
from urllib.request import Request
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .forms import CreerUtilisateur


# Create your views here.

def home(request):
    place=Placement.objects.all()
    context={'place':place}
    return render(request,'index.html',context)
def accesPage(request):
    place = Placement.objects.all()
    context = {'place': place}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('listing')
        else:
            return redirect('signin')
    return render(request,'index.html',context)


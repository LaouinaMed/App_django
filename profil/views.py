from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from listing.models import Placement

# Create your views here.
def home(request,pk):
    profil=Placement.objects.get(id=pk)
    comment=profil.comment_set.all()
    context={'profil' : profil,'comment':comment}
    return render(request,'profil.html',context)


from django.shortcuts import render
from django.shortcuts import render
from .models import homedata,homeurl
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
# Create your views here.


def index(request):
    data1=homedata.objects.all()
    data2=homeurl.objects.all()
    if(request.method=='POST'):
        email=request.POST.get('email')
        successfull_message = "You have been subscribed"
        return render(request,"index.html",{'data1':data1,'data2':data2 , "successfull_message":successfull_message})
    else:
        return render(request,"index.html",{'data1':data1,'data2':data2})



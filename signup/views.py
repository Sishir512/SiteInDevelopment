from django.shortcuts import render
from django.contrib.auth.models import User,auth

# Create your views here.

def signup(request):
    return render(request , 'signup.html')
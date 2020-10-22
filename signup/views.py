from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.method == 'POST':
        login_username = request.POST.get('login_username')
        login_password = request.POST.get('login_password')

        signup_name = request.POST.get('signup_name')
        signup_username = request.POST.get('signup_username')
        signup_email = request.POST.get('signup_email')
        signup_password = request.POST.get('signup_password')

        if(login_username is None and login_password is None):
            if get_user_model().objects.filter(username=signup_username).exists():
                messages.error(request,'The username has been taken already' , extra_tags='signup')
                return redirect('/signup#signup')
            elif get_user_model().objects.filter(email=signup_email).exists():
                messages.error(request,'The email has been used already' , extra_tags='signup')
                return redirect('/signup#signup') 
            else:
                user=get_user_model().objects.create_user(username=signup_username,password=signup_password,fullname=signup_name,email=signup_email)    
                user.save()
                return redirect('/signup')
        else:     
            user=auth.authenticate(username=login_username,password=login_password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                messages.error(request , 'Username or password not matching', extra_tags='login')
                return redirect('/signup')


    else:
        return render(request , 'signup.html')


@login_required(login_url='/signup')
def logout(request):
    auth.logout(request)
    return redirect('/')    # Redirect to the same page 
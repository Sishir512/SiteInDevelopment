from django.shortcuts import render,redirect , HttpResponse
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode , urlsafe_base64_decode
from django.utils.encoding import force_bytes , force_text
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import EditUsernameForm
# Create your views here.


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
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
                user=get_user_model().objects.create_user(username = signup_username , password = signup_password , fullname = signup_name , email = signup_email , is_active = False)    
                user.save()
                current_domain = get_current_site(request).domain
                email_message = render_to_string('accountactivationmail.html',
                {'user':user , 
                'domain':current_domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user)
                })
                email_title = 'Activate your FocusUs account'
                to_email = user.email
                email = EmailMessage(email_title , email_message , to=[to_email])
                email.send()
                return HttpResponse('Please check your email to confirm')
        else:     
            user=auth.authenticate(username=login_username,password=login_password)
            if user is not None:
                auth.login(request,user)
                next = request.GET.get('next')
                if next:
                    return redirect(next)
                return redirect('/')
            else:
                messages.error(request , 'Username or password not matching', extra_tags='login')
                return redirect('/signup')


    else:
        return render(request , 'signup.html')



def logout(request):
    auth.logout(request)
    next = request.GET.get('next')
    if next:
        return redirect(next)
    return redirect('/') 


def activate(request , uidb64 , token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user , token):
        user.is_active = True
        user.save()
        auth.login(request , user , backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponse("Your account has been confirmed")
    else:
        return HttpResponse("Your link has expired")


@login_required(login_url='/signup')
def change_username(request):
    if request.method == 'POST':
        form = EditUsernameForm(request.POST , instance = request.user)
        print('----------------')
        print(form['username'].value())
        print('----------------')
        next = request.GET.get('next')
        if form.is_valid():
            if get_user_model().objects.filter(username=form['username'].value()).exists():
                messages.error(request,'The username has been taken already')
                if next:
                    return redirect('/signup/change-username?next={}'.format(next))
                return redirect('/signup/change-username')
                
            else:
                form.save()
                if next:
                    return redirect(next)
                return redirect('/')
    
    form = EditUsernameForm(instance=request.user)
    form.initial['username']=''
    return render(request , 'setup_username.html' , {'form':form})
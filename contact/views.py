from django.shortcuts import render

# Create your views here.
thank_you_message = "Thank you for sending your message and feedback."
def contactus(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('title')
        message = request.POST.get('message')
        return render(request ,'contactus.html' , {"thank_you_message":thank_you_message})
    else:
        return render(request , 'contactus.html')
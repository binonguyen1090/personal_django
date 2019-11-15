from django.shortcuts import render
from .models import Contact
def index(request):
    return render(request, 'helloworld/index.html')

def portfolio(request):
    return render(request, 'helloworld/portfolio.html')

def contact(request):
    if request.method == "POST":
        email = (request.POST.get('email'))
        subject = (request.POST.get('subject'))
        message = (request.POST.get('message'))

        c = Contact(email=email,subject=subject,message=message)
        c.save()
        return render(request, 'helloworld/thank.html')
    else:
        return render(request, 'helloworld/contact.html')
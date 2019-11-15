from django.shortcuts import render
from .models import Contact
import requests
import json
def index(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        r = requests.get('http://api.icndb.com/jokes/random?firstName='+ fname +'&lastName='+ lname)
        data = json.loads(r.text)
        value = data['value']['joke']
        context = {'joke':value}
        return render(request, 'helloworld/index.html',context)
    else:
        f_name = 'Alo'
        l_name = "Yes"

        r = requests.get('http://api.icndb.com/jokes/random?firstName='+ f_name +'&lastName='+ l_name)
        data = json.loads(r.text)
        value = data['value']['joke']
        context = {'joke':value}
        return render(request, 'helloworld/index.html',context)

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
from django.shortcuts import render

def index(request):
    return render(request, 'helloworld/index.html')

def portfolio(request):
    return render(request, 'helloworld/portfolio.html')

def contact(request):
    return render(request, 'helloworld/contact.html')
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index/index.html')


def aboutUs(request):
    return render(request, 'index/aboutUs.html')


def contactUs(request):
    return render(request, 'index/contactUs.html')


def services(request):
    return render(request, 'index/services.html')


def enquiry(request):
    return render(request, 'index/enquiry.html')


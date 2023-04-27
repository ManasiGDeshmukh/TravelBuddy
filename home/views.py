from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def packages(request):
    return render(request, 'Packages.html')

def about(request):
    return HttpResponse("About")

def contact(request):
    return HttpResponse("Contact Us")
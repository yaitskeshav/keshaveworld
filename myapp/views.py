
# Create your views here.
from django.http import HttpResponse 
from django.shortcuts import render ,HttpResponse
from myapp.models import  Details


def index(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        city= request.POST.get('city')
        email= request.POST.get('email')
        details=Details(name=name,city=city,email=email)
        details.save()
    return render(request, 'myapp/index.html')
def evs(request):
    return render(request, 'myapp/evs.html')
def java(request):
    return render(request, 'myapp/java.html')
def cm(request):
    return render(request, 'myapp/cm.html')
def maths2(request):
    return render(request, 'myapp/maths2.html')
def physics(request):
    return render(request, 'myapp/physics.html')
def tn(request):
    return render(request, 'myapp/tn.html')
def ws(request):
    return render(request, 'myapp/works.html')
def ref(request):
    return render(request, 'myapp/ref.html')
from django.shortcuts import render
from .models import TravelPackage

# Create your views here.
def home(request):
    packages = TravelPackage.objects.all()
    return render(request, 'travel_packages/home.html', {'packages': packages})

def ofertas(request):
    packages = TravelPackage.objects.all().order_by('discounted_price')
    return render(request, 'travel_packages/ofertas.html', {'packages': packages})
from django.shortcuts import render

from .models import Product

# Create your views here.
def product_list(request):
   products=Product.objects.all()

   data = {
    'products': products
   }
   return render(request,'product_page.html',data)

def home(request):
   
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')